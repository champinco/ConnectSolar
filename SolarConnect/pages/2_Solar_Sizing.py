import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils.pvgis_api import get_irradiance_data, get_optimal_tilt_angle
from utils.solar_calculator import calculate_system_size, calculate_inverter_size, calculate_wire_sizes
import folium
from streamlit_folium import folium_static

# Import data modules
from data.kenya_counties import get_kenya_counties, get_county_regions

# Set page configuration
st.set_page_config(
    page_title="Solar System Sizing - Solar Sizing App",
    page_icon="☀️",
    layout="wide"
)

# Initialize session state for solar system results if it doesn't exist
if 'solar_system_results' not in st.session_state:
    st.session_state.solar_system_results = None
if 'location' not in st.session_state:
    st.session_state.location = None
if 'irradiance_data' not in st.session_state:
    st.session_state.irradiance_data = None

# App title
st.title("☀️ Solar System Sizing")

# Check if energy consumption has been calculated
if 'total_daily_energy' not in st.session_state or st.session_state.total_daily_energy == 0:
    st.warning("Please calculate your energy consumption first!")
    st.page_link("pages/1_Energy_Calculator.py", label="Go to Energy Calculator", icon="⚡")
else:
    # Display current energy consumption
    st.header("Your Energy Consumption")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Daily Energy Consumption", f"{st.session_state.total_daily_energy:.2f} kWh")
    with col2:
        st.metric("Monthly Energy Consumption", f"{st.session_state.total_monthly_energy:.2f} kWh")
    
    # Solar system sizing form
    st.header("Sizing Parameters")
    
    # Location selection
    st.subheader("Location Information")
    location_tab1, location_tab2 = st.tabs(["Map Selection", "Manual Entry"])
    
    with location_tab1:
        # Create a folium map centered at Kenya
        m = folium.Map(location=[-1.286389, 36.817223], zoom_start=6)
        
        # Add a click event to get coordinates
        m.add_child(folium.ClickForMarker(popup="Selected Location"))
        
        # Display the map
        st.write("Click on the map to select your location:")
        folium_static(m)
        
        # Get clicked coordinates (in a real implementation, we would capture the click event)
        # For now, we'll use manual entry for coordinates from the map
        col1, col2 = st.columns(2)
        with col1:
            latitude = st.number_input("Latitude from Map", value=-1.286389, format="%.6f")
        with col2:
            longitude = st.number_input("Longitude from Map", value=36.817223, format="%.6f")
        
        if st.button("Use This Location"):
            st.session_state.location = {
                "latitude": latitude,
                "longitude": longitude,
                "location_name": f"Custom Location ({latitude:.6f}, {longitude:.6f})"
            }
            # Get solar irradiance data from PVGIS API
            with st.spinner("Fetching solar irradiance data..."):
                irradiance_data = get_irradiance_data(latitude, longitude)
                st.session_state.irradiance_data = irradiance_data
                st.success("Location and solar data updated!")
                st.rerun()
    
    with location_tab2:
        # Get all 47 counties in Kenya
        counties = get_kenya_counties()
        regions = get_county_regions()
        
        # Create region and county selection
        st.write("### Select County")
        
        # First select region, then county
        region_options = list(regions.keys())
        selected_region = st.selectbox("Select Region", region_options)
        
        # Filter counties by region
        counties_in_region = regions[selected_region]
        county_options = ["Select County..."] + counties_in_region
        selected_county = st.selectbox("Select County", county_options)
        
        # Custom option
        use_custom = st.checkbox("Use custom location instead")
        
        if use_custom or selected_county == "Select County...":
            col1, col2 = st.columns(2)
            with col1:
                latitude = st.number_input("Latitude", format="%.6f", value=-1.286389)
            with col2:
                longitude = st.number_input("Longitude", format="%.6f", value=36.817223)
            location_name = st.text_input("Location Name", "Custom Location")
            
            location_data = {
                "latitude": latitude,
                "longitude": longitude,
                "location_name": location_name,
                "climate_data": None
            }
        else:
            # Get county data
            county_data = counties[selected_county]
            latitude = county_data["coordinates"]["latitude"]
            longitude = county_data["coordinates"]["longitude"] 
            climate_data = county_data["climate"]
            
            location_data = {
                "latitude": latitude,
                "longitude": longitude,
                "location_name": selected_county,
                "climate_data": climate_data,
                "elevation": county_data["elevation"],
                "region": county_data["region"]
            }
            
            # Display county information
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Coordinates:** {latitude:.4f}, {longitude:.4f}")
                st.write(f"**Elevation:** {county_data['elevation']} meters above sea level")
                st.write(f"**Region:** {county_data['region']}")
            
            with col2:
                st.write(f"**Peak Sun Hours:** {climate_data['peak_sun_hours']} hours/day")
                st.write(f"**Average Temperature:** {climate_data['avg_temperature']}°C")
                st.write(f"**Annual Rainfall:** {climate_data['rainfall_mm_per_year']} mm")
                st.write(f"**Average Humidity:** {climate_data['humidity_percent']}%")
        
        if st.button("Set Location", key="manual_location"):
            st.session_state.location = location_data
            
            # Use county data for peak sun hours if available, otherwise fetch from PVGIS API
            if location_data["climate_data"] is not None:
                # Create simplified irradiance data structure based on county data
                peak_sun_hours = location_data["climate_data"]["peak_sun_hours"]
                avg_monthly_irradiance = peak_sun_hours * 1000  # Convert to W/m²
                
                # Create a uniform monthly distribution as placeholder (ideally would have monthly values)
                monthly_averages = [avg_monthly_irradiance] * 12
                
                irradiance_data = {
                    "peak_sun_hours": peak_sun_hours,
                    "avg_irradiance": avg_monthly_irradiance,
                    "monthly_averages": monthly_averages,
                    "source": "Kenya Counties Database"
                }
                
                st.session_state.irradiance_data = irradiance_data
                st.success(f"Using solar data for {selected_county} County!")
            else:
                # Get solar irradiance data from PVGIS API for custom locations
                with st.spinner("Fetching solar irradiance data from PVGIS API..."):
                    irradiance_data = get_irradiance_data(latitude, longitude)
                    st.session_state.irradiance_data = irradiance_data
                    st.success("Location and solar data updated!")
            
            st.rerun()
    
    # Display solar irradiance data if available
    if st.session_state.irradiance_data:
        st.subheader(f"Solar Data for {st.session_state.location['location_name']}")
        
        # Display average solar irradiance
        avg_irradiance = np.mean(st.session_state.irradiance_data['monthly_averages'])
        peak_sun_hours = avg_irradiance / 1000  # Convert W/m² to kWh/m²/day
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Average Solar Irradiance", f"{avg_irradiance:.2f} W/m²")
        with col2:
            st.metric("Peak Sun Hours", f"{peak_sun_hours:.2f} hours/day")
        
        # Plot monthly solar irradiance
        monthly_data = st.session_state.irradiance_data['monthly_averages']
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(months, monthly_data)
        ax.set_ylabel('Solar Irradiance (W/m²)')
        ax.set_title('Monthly Average Solar Irradiance')
        
        st.pyplot(fig)
    
    # System specifications form
    st.header("System Specifications")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Usage Parameters")
        autonomy_days = st.slider("Autonomy Days (Backup)", min_value=0, max_value=5, value=1, 
                               help="Number of days the system should be able to run without sun")
        
        efficiency = st.slider("System Efficiency (%)", min_value=70, max_value=95, value=85,
                            help="Overall efficiency of the solar system including losses")
        
        future_expansion = st.slider("Future Expansion (%)", min_value=0, max_value=100, value=20,
                                  help="Additional capacity for future needs")
    
    with col2:
        st.subheader("Technical Parameters")
        battery_dod = st.slider("Battery Depth of Discharge (%)", min_value=50, max_value=95, value=80,
                             help="Maximum percentage of battery capacity that can be used")
        
        battery_voltage = st.selectbox("Battery Voltage", [12, 24, 48], index=1,
                                    help="Voltage of the battery bank")
        
        panel_wattage = st.selectbox("Solar Panel Wattage (W)", [250, 300, 330, 400, 450, 500, 550], index=3,
                                  help="Wattage of individual solar panels")
    
    # Calculate button
    if st.button("Calculate System Size", type="primary"):
        if not st.session_state.irradiance_data:
            st.error("Please set your location first to get solar irradiance data")
        else:
            with st.spinner("Calculating system size..."):
                # Calculate system size
                results = calculate_system_size(
                    daily_energy_kwh=st.session_state.total_daily_energy,
                    peak_sun_hours=peak_sun_hours,
                    panel_wattage=panel_wattage,
                    battery_voltage=battery_voltage,
                    battery_dod=battery_dod/100,  # Convert percentage to decimal
                    autonomy_days=autonomy_days,
                    system_efficiency=efficiency/100,  # Convert percentage to decimal
                    future_expansion=future_expansion/100  # Convert percentage to decimal
                )
                
                # Store results in session state
                st.session_state.solar_system_results = results
                
                st.success("Calculation complete!")
                st.rerun()
    
    # Display system size results if available
    if st.session_state.solar_system_results:
        st.header("Recommended Solar System")
        
        results = st.session_state.solar_system_results
        
        # Create three columns for key metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Solar Array Size", f"{results['total_panel_capacity_kw']:.2f} kWp")
            st.write(f"Number of Panels: {results['number_of_panels']}")
            st.write(f"Panel Wattage: {panel_wattage} W")
        
        with col2:
            st.metric("Battery Capacity", f"{results['battery_capacity_kwh']:.2f} kWh")
            st.write(f"Battery Ah: {results['battery_capacity_ah']:.2f} Ah")
            st.write(f"Battery Voltage: {battery_voltage} V")
        
        with col3:
            # In a real system, we'd calculate this based on AC vs DC loads
            inverter_size = results['total_panel_capacity_kw'] * 1.2  # 20% overhead
            st.metric("Inverter Size", f"{inverter_size:.2f} kW")
            st.write(f"System Type: Grid-tied with battery backup")
        
        # Display coverage information with a progress bar
        st.subheader("Energy Coverage")
        coverage = results.get('coverage_percentage', 100)
        st.write(f"This system will cover approximately {coverage:.1f}% of your energy needs")
        st.progress(min(coverage/100, 1.0))
        
        if 'ideal_number_of_panels' in results and results['ideal_number_of_panels'] > results['number_of_panels']:
            st.info(f"Note: The ideal system would require {results['ideal_number_of_panels']} panels, but we've limited it to a more practical size of {results['number_of_panels']} panels.")
        
        # Additional system details
        st.subheader("System Details")
        
        # Create detailed summary
        st.write(f"""
        #### Solar Array Configuration
        - Total Array Capacity: {results['total_panel_capacity_kw']:.2f} kWp
        - Number of Panels: {results['number_of_panels']}
        - Panel Type: Monocrystalline {panel_wattage}W
        - Estimated Array Area: {results['array_area_sqm']:.2f} m²
        - Energy Coverage: {coverage:.1f}%
        
        #### Battery System
        - Battery Capacity: {results['battery_capacity_kwh']:.2f} kWh / {results['battery_capacity_ah']:.2f} Ah
        - Battery Voltage: {battery_voltage} V
        - Depth of Discharge: {battery_dod}%
        - Autonomy Period: {autonomy_days} days
        
        #### System Specifications
        - Inverter Size (recommended): {inverter_size:.2f} kW
        - System Efficiency: {efficiency}%
        - Expansion Capacity: {future_expansion}%
        """)
        
        # Next steps
        st.divider()
        st.write("Ready to see cost estimates and ROI analysis?")
        st.page_link("pages/3_Cost_Comparison.py", label="Continue to Cost Analysis", icon="💰")
