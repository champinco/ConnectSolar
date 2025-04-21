import streamlit as st
import pandas as pd
import numpy as np
from data.installers import get_installers

# Set page configuration
st.set_page_config(
    page_title="Solar Installer Directory - Solar Sizing App",
    page_icon="👷",
    layout="wide"
)

# App title
st.title("👷 Solar Installer Directory")

# Get installer data
installers = get_installers()

# Create installer dataframe
installer_df = pd.DataFrame(installers)

# Sidebar for filtering options
st.sidebar.header("Filter Installers")

# Region filter
regions = ["All Regions"] + sorted(installer_df["region"].unique().tolist())
selected_region = st.sidebar.selectbox("Select Region", regions)

# Experience filter
min_experience = st.sidebar.slider("Minimum Years of Experience", 0, 20, 0)

# Certification filter
certifications = ["All"] + sorted(
    set([cert for sublist in installer_df["certifications"].tolist() for cert in sublist])
)
selected_certification = st.sidebar.selectbox("Certification", certifications)

# System type filter
system_types = ["All"] + sorted(
    set([system_type for sublist in installer_df["system_types"].tolist() for system_type in sublist])
)
selected_system_type = st.sidebar.selectbox("System Type", system_types)

# Apply filters
filtered_df = installer_df.copy()

if selected_region != "All Regions":
    filtered_df = filtered_df[filtered_df["region"] == selected_region]

if min_experience > 0:
    filtered_df = filtered_df[filtered_df["years_experience"] >= min_experience]

if selected_certification != "All":
    filtered_df = filtered_df[filtered_df["certifications"].apply(lambda x: selected_certification in x)]

if selected_system_type != "All":
    filtered_df = filtered_df[filtered_df["system_types"].apply(lambda x: selected_system_type in x)]

# Main content
st.header("Find Qualified Solar Installers in Kenya")

# Intro text
st.write("""
Find vetted, qualified solar system installers across Kenya. All installers in our directory have been verified 
and have proven experience in solar PV system installation.

**How to use this directory:**
1. Filter installers by region, experience, certifications, and system types using the sidebar
2. Review installer profiles, experience, and ratings
3. Contact installers directly or request quotes through our platform
""")

# Display number of matching installers
st.subheader(f"Found {len(filtered_df)} matching installers")

# Check if we have any installers after filtering
if len(filtered_df) == 0:
    st.warning("No installers match your filter criteria. Please try different filters.")
else:
    # Display installers as cards
    for index, installer in filtered_df.iterrows():
        # Create a card-like container
        with st.container():
            col1, col2 = st.columns([1, 3])
            
            with col1:
                # Display rating as stars
                rating = "⭐" * int(installer["rating"])
                st.image("https://upload.wikimedia.org/wikipedia/commons/e/e7/Noun_Project_Solar_Panel_icon_2891451.svg", width=120)
                st.write(f"**Rating:** {rating} ({installer['rating']}/5)")
            
            with col2:
                st.subheader(installer["name"])
                st.write(f"**Location:** {installer['region']}, Kenya")
                st.write(f"**Experience:** {installer['years_experience']} years")
                st.write(f"**Certifications:** {', '.join(installer['certifications'])}")
                st.write(f"**Specializes in:** {', '.join(installer['system_types'])}")
                
                # Show contact information
                st.write(f"📞 {installer['phone']}")
                st.write(f"✉️ {installer['email']}")
                
                # Show completed projects count
                st.write(f"**Completed Projects:** {installer['completed_projects']}")
                
                # Contact button
                st.button(f"Request Quote from {installer['name']}", key=f"contact_{index}")
            
            # Add a separator between installers
            st.divider()
    
    # Request for installation form
    st.header("Request Installation Quotes")
    
    st.write("""
    Fill out this form to request quotes from multiple installers in your area. Your solar system
    specifications will be shared with qualified installers who will contact you with competitive quotes.
    """)
    
    # Check if we have solar system results in session state
    if 'solar_system_results' in st.session_state and st.session_state.solar_system_results is not None:
        st.info("We'll include your solar system specifications in your quote request")
        
        # Display system summary
        results = st.session_state.solar_system_results
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Solar Array Size", f"{results['total_panel_capacity_kw']:.2f} kWp")
        
        with col2:
            st.metric("Battery Capacity", f"{results['battery_capacity_kwh']:.2f} kWh")
        
        with col3:
            inverter_size = results['total_panel_capacity_kw'] * 1.2  # 20% overhead
            st.metric("Inverter Size", f"{inverter_size:.2f} kW")
    else:
        st.warning("You haven't sized a solar system yet. Consider sizing your system before requesting quotes.")
        st.page_link("pages/2_Solar_Sizing.py", label="Go to Solar Sizing", icon="☀️")
    
    # Form for requesting quotes
    with st.form("quote_request_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Your Name")
            email = st.text_input("Email Address")
            phone = st.text_input("Phone Number")
        
        with col2:
            location = st.text_input("Your Location (City/Town)")
            installation_time = st.selectbox("When do you need installation?", 
                                         ["As soon as possible", "Within 1 month", "Within 3 months", "Just exploring"])
            special_requirements = st.text_area("Special Requirements (optional)")
        
        # Select installers to contact
        st.subheader("Select Installers to Contact")
        
        installer_options = {installer["name"]: False for _, installer in filtered_df.iterrows()}
        
        # Create columns to display installer checkboxes in multiple columns
        num_cols = 3
        cols = st.columns(num_cols)
        
        for i, (installer_name, _) in enumerate(installer_options.items()):
            with cols[i % num_cols]:
                installer_options[installer_name] = st.checkbox(installer_name)
        
        # Select all option
        select_all = st.checkbox("Select All Installers")
        if select_all:
            for name in installer_options:
                installer_options[name] = True
        
        submitted = st.form_submit_button("Submit Quote Request")
        
        if submitted:
            if not name or not email or not phone or not location:
                st.error("Please fill out all required fields")
            else:
                selected_installers = [name for name, selected in installer_options.items() if selected]
                
                if not selected_installers:
                    st.error("Please select at least one installer")
                else:
                    st.success(f"Your quote request has been sent to {len(selected_installers)} installers. They will contact you shortly!")
                    
                    # In a real app, we would send this data to a backend service
                    st.write("**Request Details:**")
                    st.write(f"Name: {name}")
                    st.write(f"Contact: {email} / {phone}")
                    st.write(f"Location: {location}")
                    st.write(f"Installation Timeframe: {installation_time}")
                    st.write(f"Selected Installers: {', '.join(selected_installers)}")
    
    # Additional information about selecting installers
    st.header("Tips for Selecting a Solar Installer")
    
    st.write("""
    ### What to Look for in a Solar Installer
    
    When selecting a solar installer, consider the following factors:
    
    1. **Experience & Expertise**: Look for installers with extensive experience in solar PV systems, especially in Kenya.
    
    2. **Certifications**: Verify that installers have relevant certifications such as:
       - Energy Regulatory Commission (ERC) license
       - Solar PV System Professional Certification
       - Electrical Contractor License
    
    3. **References & Portfolio**: Ask for references or examples of previous installations similar to your requirements.
    
    4. **Warranty & Support**: Inquire about warranties for equipment and installation, as well as ongoing maintenance support.
    
    5. **Competitive Pricing**: Compare quotes from multiple installers, but be wary of significantly lower prices that might indicate lower quality components.
    
    6. **Comprehensive Services**: Choose installers who offer end-to-end services, from design to installation and maintenance.
    
    7. **Local Knowledge**: Local installers will be familiar with Kenya's regulations, climate conditions, and available incentives.
    """)

# Footer
st.divider()
st.caption("Kenya Solar System Sizing App - Connecting Kenyans with qualified solar professionals")
