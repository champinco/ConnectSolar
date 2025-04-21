import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils.roi_calculator import calculate_roi, calculate_grid_costs
from utils.pdf_generator import generate_pdf_report
from data.kenya_electricity_tariffs import get_electricity_tariff
import io
import base64
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Cost Comparison - Solar Sizing App",
    page_icon="💰",
    layout="wide"
)

# Initialize session state variables for cost analysis if they don't exist
if 'cost_analysis_results' not in st.session_state:
    st.session_state.cost_analysis_results = None

# App title
st.title("💰 Cost Comparison & ROI Analysis")

# Check if solar system has been sized
if 'solar_system_results' not in st.session_state or st.session_state.solar_system_results is None:
    st.warning("Please size your solar system first!")
    st.page_link("pages/2_Solar_Sizing.py", label="Go to Solar Sizing", icon="☀️")
else:
    # Display current solar system summary
    st.header("Your Solar System")
    
    results = st.session_state.solar_system_results
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Solar Array Size", f"{results['total_panel_capacity_kw']:.2f} kWp")
    
    with col2:
        st.metric("Battery Capacity", f"{results['battery_capacity_kwh']:.2f} kWh")
    
    with col3:
        inverter_size = results['total_panel_capacity_kw'] * 1.2  # 20% overhead
        st.metric("Inverter Size", f"{inverter_size:.2f} kW")
    
    # Cost estimation form
    st.header("Cost Estimation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Solar System Costs")
        panel_cost_per_wp = st.number_input("Solar Panel Cost (KES/Wp)", min_value=50, max_value=200, value=90,
                                         help="Cost per watt peak for solar panels")
        
        battery_cost_per_kwh = st.number_input("Battery Cost (KES/kWh)", min_value=20000, max_value=100000, value=40000,
                                           help="Cost per kWh for battery storage")
        
        inverter_cost_per_kw = st.number_input("Inverter Cost (KES/kW)", min_value=15000, max_value=80000, value=30000,
                                           help="Cost per kW for inverter")
        
        installation_percent = st.slider("Installation Cost (%)", min_value=10, max_value=30, value=15,
                                     help="Installation cost as percentage of equipment cost")
        
        maintenance_annual = st.number_input("Annual Maintenance (KES)", min_value=5000, max_value=50000, value=10000,
                                         help="Annual maintenance cost for solar system")
        
        battery_replacement_years = st.slider("Battery Replacement (years)", min_value=5, max_value=15, value=10,
                                        help="Expected battery replacement interval in years")
    
    with col2:
        st.subheader("Grid Electricity Parameters")
        
        # Check if we have custom tariff from bill
        has_custom_tariff = 'custom_tariff' in st.session_state and st.session_state.custom_tariff
        
        # Get user preference for tariff source
        tariff_source = "From Bill" if has_custom_tariff else "Standard Tariffs"
        tariff_source = st.radio(
            "Tariff Source",
            ["Standard Tariffs", "From Bill", "Custom Input"],
            index=0 if not has_custom_tariff else 1,
            horizontal=True,
            help="Choose whether to use standard Kenya Power tariffs, tariff extracted from your bill, or enter custom values"
        )
        
        if tariff_source == "Standard Tariffs":
            # Select tariff type
            consumer_type = st.selectbox("Consumer Type", ["Domestic", "Small Commercial", "Commercial (DC)", "Industrial"])
            
            # Get tariff based on selection
            tariff_info = get_electricity_tariff(consumer_type)
            
            # Display tariff information
            st.write(f"**Tariff Rate:** KES {tariff_info['energy_charge']}/kWh")
            st.write(f"**Fixed Charge:** KES {tariff_info['fixed_charge']}/month")
            
            energy_charge = float(tariff_info['energy_charge'])
            fixed_charge = int(tariff_info['fixed_charge'])
            
        elif tariff_source == "From Bill" and has_custom_tariff:
            # Use tariff information extracted from bill
            bill_tariff = st.session_state.custom_tariff
            
            # Display the tariff info from the bill
            st.write(f"**Tariff Rate from Bill:** KES {bill_tariff['energy_charge']}/kWh")
            st.write(f"**Fixed Charge from Bill:** KES {bill_tariff['fixed_charge']}/month")
            
            energy_charge = float(bill_tariff['energy_charge'])
            fixed_charge = int(bill_tariff['fixed_charge'])
            
        else:  # Custom Input
            # Allow custom input of rates
            energy_charge = st.number_input(
                "Energy Charge (KES/kWh)", 
                min_value=5.0, 
                max_value=50.0, 
                value=21.0 if not has_custom_tariff else float(st.session_state.custom_tariff['energy_charge']),
                step=0.1
            )
            fixed_charge = st.number_input(
                "Fixed Charge (KES/month)", 
                min_value=0, 
                max_value=5000, 
                value=200 if not has_custom_tariff else int(st.session_state.custom_tariff['fixed_charge'])
            )
        
        # Grid electricity inflation rate
        grid_inflation = st.slider("Grid Electricity Inflation (%/year)", min_value=2, max_value=15, value=5,
                                help="Estimated annual increase in electricity costs")
        
        # Analysis period
        analysis_period = st.slider("Analysis Period (years)", min_value=5, max_value=25, value=20,
                                 help="Period over which to compare solar vs grid costs")
    
    # Calculate button
    if st.button("Calculate ROI & Cost Comparison", type="primary"):
        with st.spinner("Calculating costs and ROI..."):
            # Calculate solar system costs
            panel_cost = results['total_panel_capacity_kw'] * 1000 * panel_cost_per_wp
            battery_cost = results['battery_capacity_kwh'] * battery_cost_per_kwh
            inverter_cost = inverter_size * inverter_cost_per_kw
            
            equipment_cost = panel_cost + battery_cost + inverter_cost
            installation_cost = equipment_cost * (installation_percent / 100)
            
            total_initial_cost = equipment_cost + installation_cost
            
            # Calculate grid electricity costs
            monthly_energy_kwh = st.session_state.total_monthly_energy
            annual_energy_kwh = monthly_energy_kwh * 12
            
            grid_costs = calculate_grid_costs(
                annual_energy_kwh=annual_energy_kwh,
                energy_charge=energy_charge,
                fixed_charge=fixed_charge,
                inflation_rate=grid_inflation/100,  # Convert percentage to decimal
                years=analysis_period
            )
            
            # Calculate ROI and payback period
            roi_results = calculate_roi(
                total_initial_cost=total_initial_cost,
                annual_maintenance=maintenance_annual,
                battery_replacement_cost=battery_cost,
                battery_replacement_years=battery_replacement_years,
                grid_costs=grid_costs,
                analysis_period=analysis_period
            )
            
            # Store results in session state
            st.session_state.cost_analysis_results = {
                "panel_cost": panel_cost,
                "battery_cost": battery_cost,
                "inverter_cost": inverter_cost,
                "equipment_cost": equipment_cost,
                "installation_cost": installation_cost,
                "total_initial_cost": total_initial_cost,
                "maintenance_annual": maintenance_annual,
                "battery_replacement_years": battery_replacement_years,
                "grid_costs": grid_costs,
                "roi_results": roi_results,
                "energy_charge": energy_charge,
                "fixed_charge": fixed_charge,
                "grid_inflation": grid_inflation,
                "analysis_period": analysis_period
            }
            
            st.success("Calculation complete!")
            st.rerun()
    
    # Display cost analysis results if available
    if st.session_state.cost_analysis_results:
        st.header("Cost Analysis Results")
        
        results = st.session_state.cost_analysis_results
        
        # Display initial costs
        st.subheader("Initial Solar System Investment")
        
        # Add financing options
        financing_option = st.radio(
            "Payment Option",
            ["Cash Purchase", "Financing (Solar Loan)"],
            horizontal=True,
            help="Choose between paying the full amount upfront or financing through a solar loan"
        )
        
        if financing_option == "Financing (Solar Loan)":
            col1, col2, col3 = st.columns(3)
            with col1:
                down_payment_percent = st.slider("Down Payment (%)", min_value=10, max_value=50, value=30,
                                          help="Percentage of the total cost paid upfront")
            with col2:
                loan_term_years = st.slider("Loan Term (years)", min_value=3, max_value=10, value=7,
                                       help="Duration of the solar loan")
            with col3:
                interest_rate = st.slider("Interest Rate (%)", min_value=6, max_value=20, value=12,
                                     help="Annual interest rate on the solar loan")
            
            # Update ROI calculation with new financing parameters
            if 'total_initial_cost' in results:
                financing_percentage = (100 - down_payment_percent) / 100
                roi_data = calculate_roi(
                    total_initial_cost=results['total_initial_cost'],
                    annual_maintenance=results['maintenance_annual'],
                    battery_replacement_cost=results['battery_cost'],
                    battery_replacement_years=results['battery_replacement_years'],
                    grid_costs=results['grid_costs'],
                    analysis_period=results['analysis_period'],
                    financing_percentage=financing_percentage,
                    financing_years=loan_term_years,
                    financing_interest=interest_rate/100
                )
                results['roi_results'] = roi_data
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Solar Panels", f"KES {results['panel_cost']:,.2f}")
            st.write(f"({st.session_state.solar_system_results['total_panel_capacity_kw']:.2f} kWp @ KES {panel_cost_per_wp}/Wp)")
        
        with col2:
            st.metric("Battery System", f"KES {results['battery_cost']:,.2f}")
            st.write(f"({st.session_state.solar_system_results['battery_capacity_kwh']:.2f} kWh @ KES {battery_cost_per_kwh}/kWh)")
        
        with col3:
            st.metric("Inverter", f"KES {results['inverter_cost']:,.2f}")
            st.write(f"({inverter_size:.2f} kW @ KES {inverter_cost_per_kw}/kW)")
        
        st.metric("Installation Cost", f"KES {results['installation_cost']:,.2f}")
        st.metric("Total System Cost", f"KES {results['total_initial_cost']:,.2f}")
        
        roi_data = results['roi_results']
        
        # Display financing details if applicable
        if financing_option == "Financing (Solar Loan)" and 'financing_details' in roi_data:
            st.subheader("Financing Details")
            fin = roi_data['financing_details']
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Down Payment", f"KES {fin['down_payment']:,.2f}")
                st.metric("Loan Amount", f"KES {fin['financed_amount']:,.2f}")
            with col2:
                st.metric("Monthly Payment", f"KES {fin['monthly_payment']:,.2f}")
                st.metric("Loan Term", f"{fin['financing_years']} years")
        
        # Display ROI summary
        st.subheader("Return on Investment")
        
        # First year savings
        if 'first_year_savings' in roi_data:
            st.subheader("First Year Savings")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Monthly Savings", f"KES {roi_data['monthly_first_year_savings']:,.2f}")
                
            with col2:
                st.metric("First Year Savings", f"KES {roi_data['first_year_savings']:,.2f}")
                
            with col3:
                first_year_percentage = roi_data.get('first_year_savings_percentage', 0)
                st.metric("Bill Reduction", f"{first_year_percentage:.1f}%")
                
            # Add emphasis if there are immediate savings
            if roi_data['first_year_savings'] > 0:
                st.success(f"You'll start saving from day one! Your electricity bill will be reduced by approximately {first_year_percentage:.1f}% in the first year.")
        
        # Long-term benefits
        st.subheader("Long-term Benefits")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Payback Period", f"{roi_data['payback_period']:.1f} years")
        
        with col2:
            st.metric("Lifetime Savings", f"KES {roi_data['total_savings']:,.2f}")
        
        with col3:
            st.metric("ROI (%)", f"{roi_data['roi_percent']:.1f}%")
        
        # Grid vs Solar comparison over time
        st.subheader("Grid vs Solar: Cumulative Cost Comparison")
        
        # Prepare data for plotting
        years = list(range(1, results['analysis_period'] + 1))
        grid_costs_cumulative = np.cumsum(results['grid_costs']['annual_costs'])
        solar_costs_cumulative = [results['total_initial_cost']]
        
        # Add annual maintenance costs and battery replacements
        for year in range(1, results['analysis_period']):
            annual_cost = results['maintenance_annual']
            
            # Add battery replacement cost if needed
            if year % results['battery_replacement_years'] == 0 and year > 0:
                annual_cost += results['battery_cost']
            
            solar_costs_cumulative.append(solar_costs_cumulative[-1] + annual_cost)
        
        # Plot cumulative costs
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(years, grid_costs_cumulative, 'b-', label='Grid Electricity')
        ax.plot(years, solar_costs_cumulative, 'g-', label='Solar System')
        
        # Mark the intersection point (payback period)
        payback_period = roi_data['payback_period']
        if payback_period <= results['analysis_period']:
            # Find the approximate intersection point
            payback_year = int(payback_period)
            payback_fraction = payback_period - payback_year
            
            if payback_year < len(solar_costs_cumulative):
                if payback_year > 0:
                    payback_cost = solar_costs_cumulative[payback_year-1] + (solar_costs_cumulative[payback_year] - solar_costs_cumulative[payback_year-1]) * payback_fraction
                else:
                    payback_cost = solar_costs_cumulative[0] * payback_fraction
                
                ax.plot(payback_period, payback_cost, 'ro', markersize=8)
                ax.annotate(f'Payback: {payback_period:.1f} years', 
                            xy=(payback_period, payback_cost),
                            xytext=(payback_period+1, payback_cost),
                            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))
        
        ax.set_xlabel('Years')
        ax.set_ylabel('Cumulative Cost (KES)')
        ax.set_title('Grid vs Solar: Cumulative Cost Over Time')
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Yearly cost breakdown
        st.subheader("Yearly Cost Comparison")
        
        # Create a DataFrame for the yearly costs
        yearly_data = []
        
        for year in range(1, results['analysis_period'] + 1):
            solar_annual_cost = results['maintenance_annual']
            
            # Add battery replacement cost if needed
            if year % results['battery_replacement_years'] == 0:
                solar_annual_cost += results['battery_cost']
            
            if year == 1:
                solar_annual_cost += results['total_initial_cost']
            
            yearly_data.append({
                'Year': year,
                'Grid Cost (KES)': results['grid_costs']['annual_costs'][year-1],
                'Solar Cost (KES)': solar_annual_cost,
                'Annual Savings (KES)': results['grid_costs']['annual_costs'][year-1] - solar_annual_cost,
                'Cumulative Grid Cost (KES)': grid_costs_cumulative[year-1],
                'Cumulative Solar Cost (KES)': solar_costs_cumulative[year-1],
                'Cumulative Savings (KES)': grid_costs_cumulative[year-1] - solar_costs_cumulative[year-1]
            })
        
        yearly_df = pd.DataFrame(yearly_data)
        
        # Show the dataframe
        st.dataframe(yearly_df)
        
        # Generate PDF report
        st.header("Generate PDF Report")
        
        # Allow user to enter name and contact details for the report
        col1, col2 = st.columns(2)
        with col1:
            customer_name = st.text_input("Your Name")
            customer_email = st.text_input("Your Email")
        with col2:
            customer_phone = st.text_input("Your Phone Number")
            report_date = st.date_input("Report Date", datetime.now())
        
        if st.button("Generate PDF Report"):
            if not customer_name:
                st.error("Please enter your name for the report")
            else:
                with st.spinner("Generating PDF report..."):
                    # Gather all data needed for the report
                    report_data = {
                        "customer_info": {
                            "name": customer_name,
                            "email": customer_email,
                            "phone": customer_phone,
                            "date": report_date.strftime("%Y-%m-%d")
                        },
                        "energy_usage": {
                            "daily_kwh": st.session_state.total_daily_energy,
                            "monthly_kwh": st.session_state.total_monthly_energy
                        },
                        "location": st.session_state.location,
                        "solar_sizing": st.session_state.solar_system_results,
                        "cost_analysis": st.session_state.cost_analysis_results,
                        "roi_data": roi_data,
                        "yearly_comparison": yearly_df
                    }
                    
                    # Generate the PDF report
                    pdf_bytes = generate_pdf_report(report_data)
                    
                    # Create a download button for the PDF
                    b64_pdf = base64.b64encode(pdf_bytes).decode()
                    href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="solar_system_report.pdf">Download PDF Report</a>'
                    st.markdown(href, unsafe_allow_html=True)
                    
                    st.success("PDF report generated successfully!")
        
        # Next steps
        st.divider()
        st.write("Ready to find qualified installers for your solar system?")
        st.page_link("pages/4_Installer_Directory.py", label="Find Installers", icon="👷")
