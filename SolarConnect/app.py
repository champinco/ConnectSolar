import streamlit as st
import pandas as pd
import numpy as np
from utils.pvgis_api import get_irradiance_data
from utils.solar_calculator import calculate_system_size
from utils.energy_calculator import calculate_energy_from_appliances
from utils.roi_calculator import calculate_roi
from utils.pdf_generator import generate_pdf_report

# Set page configuration
st.set_page_config(
    page_title="Solar Sizing App - Kenya",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App title
st.title("☀️ Kenya Solar System Sizing App")

# Introduction
st.markdown("""
Welcome to the Kenya Solar System Sizing App! This tool helps you determine the right solar system 
for your needs based on your energy consumption, location, and budget.

**What you can do with this app:**
- Calculate your energy usage from appliances or by uploading your energy bill
- Determine the optimal solar system size for your needs
- Compare costs between solar and grid electricity
- Analyze return on investment (ROI)
- Find qualified solar installers in your area
- Generate comprehensive reports

Get started by selecting options from the sidebar!
""")

# Main page content
st.header("Quick Start Guide")

# Create three columns
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. Calculate Energy Usage")
    st.write("""
    Start by determining your energy consumption:
    - List your appliances and usage patterns
    - OR upload your electricity bill
    """)
    st.page_link("pages/1_Energy_Calculator.py", label="Energy Calculator", icon="🔌")

with col2:
    st.subheader("2. Size Your Solar System")
    st.write("""
    Get personalized recommendations for:
    - Solar panel capacity
    - Battery storage needs
    - Inverter specifications
    """)
    st.page_link("pages/2_Solar_Sizing.py", label="Solar Sizing", icon="☀️")

with col3:
    st.subheader("3. Compare & Connect")
    st.write("""
    - Compare costs with grid electricity
    - Calculate your payback period
    - Connect with verified installers
    - Generate detailed PDF reports
    """)
    st.page_link("pages/3_Cost_Comparison.py", label="Cost Comparison", icon="💰")
    st.page_link("pages/4_Installer_Directory.py", label="Find Installers", icon="👷")

# Footer
st.divider()
st.caption("Kenya Solar System Sizing App - Helping Kenyans transition to clean, renewable energy")
