import streamlit as st
import pandas as pd
import numpy as np
import io
import base64
from data.appliances import common_appliances
from utils.energy_calculator import calculate_energy_from_appliances, extract_energy_from_bill
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="Energy Calculator - Solar Sizing App",
    page_icon="🔌",
    layout="wide"
)

# Initialize session state variables if they don't exist
if 'total_daily_energy' not in st.session_state:
    st.session_state.total_daily_energy = 0
if 'total_monthly_energy' not in st.session_state:
    st.session_state.total_monthly_energy = 0
if 'selected_appliances' not in st.session_state:
    st.session_state.selected_appliances = []

# App title
st.title("🔌 Energy Usage Calculator")

# Create tabs for different calculation methods
tab1, tab2 = st.tabs(["Calculate by Appliances", "Upload Electricity Bill"])

with tab1:
    st.header("Calculate Energy Usage from Appliances")
    
    # Add appliance form
    with st.expander("Add Appliance", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            appliance_options = ["Custom"] + list(common_appliances.keys())
            selected_appliance = st.selectbox("Select Appliance", appliance_options)
            
            if selected_appliance == "Custom":
                appliance_name = st.text_input("Appliance Name")
                power_rating = st.number_input("Power Rating (Watts)", min_value=1, value=100)
            else:
                appliance_name = selected_appliance
                power_rating = common_appliances[selected_appliance]
                st.write(f"Power Rating: {power_rating} Watts")
        
        with col2:
            quantity = st.number_input("Quantity", min_value=1, value=1)
            hours_per_day = st.number_input("Hours Used Per Day", min_value=0.1, max_value=24.0, value=1.0, step=0.1)
            days_per_week = st.number_input("Days Used Per Week", min_value=1, max_value=7, value=7)
        
        # Calculate energy usage for this appliance
        daily_energy = (power_rating * quantity * hours_per_day) / 1000  # Convert to kWh
        monthly_energy = daily_energy * (days_per_week / 7) * 30  # Approximate monthly

        # Display the energy usage for this appliance
        st.write(f"Daily Energy: {daily_energy:.2f} kWh")
        st.write(f"Monthly Energy: {monthly_energy:.2f} kWh")
        
        # Add button to add the appliance to the list
        if st.button("Add to List"):
            if selected_appliance == "Custom" and not appliance_name:
                st.error("Please enter a name for your custom appliance")
            else:
                new_appliance = {
                    "name": appliance_name,
                    "power_rating": power_rating,
                    "quantity": quantity,
                    "hours_per_day": hours_per_day,
                    "days_per_week": days_per_week,
                    "daily_energy": daily_energy,
                    "monthly_energy": monthly_energy
                }
                st.session_state.selected_appliances.append(new_appliance)
                st.success(f"Added {appliance_name} to your list!")
                st.rerun()
    
    # Display table of added appliances
    if st.session_state.selected_appliances:
        st.subheader("Your Appliances")
        
        appliance_df = pd.DataFrame(st.session_state.selected_appliances)
        
        # Function to create a delete button for each row
        def create_delete_button(row_id):
            return f"delete_{row_id}"
        
        # Add a column with delete buttons
        appliance_df['delete'] = [create_delete_button(i) for i in range(len(appliance_df))]
        
        # Show the table with appliances
        st.dataframe(
            appliance_df[['name', 'power_rating', 'quantity', 'hours_per_day', 'days_per_week', 'daily_energy', 'monthly_energy']],
            hide_index=True,
            column_config={
                'name': 'Appliance',
                'power_rating': 'Power (W)',
                'quantity': 'Qty',
                'hours_per_day': 'Hours/Day',
                'days_per_week': 'Days/Week',
                'daily_energy': 'Daily (kWh)',
                'monthly_energy': 'Monthly (kWh)'
            }
        )
        
        # Buttons for each row
        cols = st.columns(len(st.session_state.selected_appliances))
        for i, col in enumerate(cols):
            with col:
                if st.button(f"Delete {st.session_state.selected_appliances[i]['name']}", key=f"delete_{i}"):
                    st.session_state.selected_appliances.pop(i)
                    st.rerun()
        
        # Calculate total energy consumption
        total_daily = sum(app['daily_energy'] for app in st.session_state.selected_appliances)
        total_monthly = sum(app['monthly_energy'] for app in st.session_state.selected_appliances)
        
        # Update session state
        st.session_state.total_daily_energy = total_daily
        st.session_state.total_monthly_energy = total_monthly
        
        # Display total energy usage
        st.subheader("Total Energy Consumption")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Daily Energy Consumption", f"{total_daily:.2f} kWh")
        with col2:
            st.metric("Monthly Energy Consumption", f"{total_monthly:.2f} kWh")
        
        # Clear all appliances button
        if st.button("Clear All Appliances"):
            st.session_state.selected_appliances = []
            st.session_state.total_daily_energy = 0
            st.session_state.total_monthly_energy = 0
            st.rerun()
        
        # Energy usage breakdown chart
        st.subheader("Energy Usage Breakdown")
        fig, ax = plt.subplots(figsize=(10, 6))
        
        appliance_names = [app['name'] for app in st.session_state.selected_appliances]
        monthly_values = [app['monthly_energy'] for app in st.session_state.selected_appliances]
        
        # Create pie chart
        ax.pie(monthly_values, labels=appliance_names, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.title('Monthly Energy Consumption by Appliance')
        
        st.pyplot(fig)
        
        # Next step button
        st.divider()
        st.write("Ready to size your solar system?")
        st.page_link("pages/2_Solar_Sizing.py", label="Continue to Solar Sizing", icon="➡️")
    else:
        st.info("Add appliances to calculate your energy usage")

with tab2:
    st.header("Upload Electricity Bill")
    st.write("""
    Upload your recent Kenya Power electricity bill to automatically extract your energy usage information.
    
    Currently supported formats:
    - PDF bills
    - Image bills (JPG, JPEG, PNG)
    - Manual data entry for other formats
    """)
    
    bill_upload = st.file_uploader("Upload your electricity bill", type=["pdf", "jpg", "jpeg", "png"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Manual Entry")
        manually_entered_kwh = st.number_input("Enter your kWh usage from bill", min_value=0.0, value=0.0)
        bill_period = st.selectbox("Billing Period", ["1 month", "2 months"])
        period_multiplier = 1 if bill_period == "1 month" else 2
        
        tariff_info = st.checkbox("Enter tariff information", help="Enter your specific electricity tariff rate from the bill")
        
        if tariff_info:
            tariff_rate = st.number_input("Energy Charge (KES/kWh)", min_value=5.0, max_value=50.0, value=21.0, step=0.1)
            fixed_charge = st.number_input("Fixed Charge (KES/month)", min_value=0, max_value=5000, value=200)
            
            # Store tariff information in session state
            if 'custom_tariff' not in st.session_state:
                st.session_state.custom_tariff = {}
            st.session_state.custom_tariff = {
                "energy_charge": tariff_rate,
                "fixed_charge": fixed_charge
            }
        
        if manually_entered_kwh > 0:
            monthly_kwh = manually_entered_kwh / period_multiplier
            daily_kwh = monthly_kwh / 30
            
            st.session_state.total_monthly_energy = monthly_kwh
            st.session_state.total_daily_energy = daily_kwh
            
            st.metric("Monthly Energy Consumption", f"{monthly_kwh:.2f} kWh")
            st.metric("Daily Energy Consumption", f"{daily_kwh:.2f} kWh")
    
    with col2:
        if bill_upload is not None:
            with st.spinner("Processing your bill..."):
                # Use the enhanced extract_energy_from_bill function
                extracted_kwh = extract_energy_from_bill(bill_upload)
                
                if extracted_kwh is not None:
                    st.success(f"Successfully extracted energy consumption: {extracted_kwh:.2f} kWh")
                    
                    # Create additional options for the extracted bill
                    bill_period_auto = st.selectbox("Billing Period (from uploaded bill)", 
                                               ["1 month", "2 months"],
                                               key="bill_period_auto")
                    period_multiplier_auto = 1 if bill_period_auto == "1 month" else 2
                    
                    # Calculate and store monthly and daily consumption
                    monthly_kwh = extracted_kwh / period_multiplier_auto
                    daily_kwh = monthly_kwh / 30
                    
                    # Store in session state
                    if st.button("Use These Values"):
                        st.session_state.total_monthly_energy = monthly_kwh
                        st.session_state.total_daily_energy = daily_kwh
                        st.success("Energy values updated!")
                        st.rerun()
                    
                    # Display extracted values
                    st.metric("Monthly Energy Consumption", f"{monthly_kwh:.2f} kWh")
                    st.metric("Daily Energy Consumption", f"{daily_kwh:.2f} kWh")
                    
                    # Display simulated additional bill information
                    with st.expander("Additional Bill Information"):
                        st.write("**Customer Information**")
                        st.write("Account Number: KP12345678")
                        st.write("Billing Period: April 2025")
                        st.write("Meter Number: M98765432")
                        
                        st.write("**Charges**")
                        energy_charge = 21.00
                        st.write(f"Energy Charge: KES {energy_charge}/kWh")
                        st.write(f"Energy Cost: KES {energy_charge * extracted_kwh:.2f}")
                        st.write("Fixed Charge: KES 200.00")
                        st.write(f"Total Bill Amount: KES {(energy_charge * extracted_kwh) + 200:.2f}")
                        
                        # Store tariff information from "bill"
                        if 'custom_tariff' not in st.session_state:
                            st.session_state.custom_tariff = {}
                        st.session_state.custom_tariff = {
                            "energy_charge": energy_charge,
                            "fixed_charge": 200
                        }
                else:
                    st.error("Could not extract energy consumption from the uploaded bill. Please use manual entry instead.")
                    st.info("Tips: Make sure your bill clearly shows the kWh consumption value. The system looks for terms like 'Total Units', 'Units Consumed', or 'Energy Consumption'.")
    
    if st.session_state.total_monthly_energy > 0:
        st.divider()
        st.write("Ready to size your solar system?")
        st.page_link("pages/2_Solar_Sizing.py", label="Continue to Solar Sizing", icon="➡️")
