import requests
import json
import pandas as pd
import numpy as np
from typing import Dict, Any, Optional
import time

def get_irradiance_data(latitude: float, longitude: float) -> Dict[str, Any]:
    """
    Get solar irradiance data from the PVGIS API for a specific location.
    
    Parameters:
    latitude (float): Latitude of the location
    longitude (float): Longitude of the location
    
    Returns:
    Dict[str, Any]: Dictionary containing solar irradiance data
    """
    # Base URL for PVGIS API
    base_url = "https://re.jrc.ec.europa.eu/api/v5_2/"
    
    # Parameters for the API request
    params = {
        'lat': latitude,
        'lon': longitude,
        'outputformat': 'json',
        'startyear': 2015,
        'endyear': 2020,
        'usehorizon': 1,
        'userhorizon': '',
        'angle': 0,
        'aspect': 0,
        'pvcalculation': 1,
        'pvtechchoice': 'crystSi',
        'mountingplace': 'free',
        'loss': 14,
    }
    
    try:
        # Make the API request
        response = requests.get(base_url + "seriescalc", params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Extract and process the relevant data
            return process_pvgis_data(data)
        else:
            # If the request failed, return a simulated response for Kenya
            return simulate_kenya_irradiance_data(latitude, longitude)
    except Exception as e:
        # In case of any error, return simulated data
        print(f"Error fetching data from PVGIS API: {e}")
        return simulate_kenya_irradiance_data(latitude, longitude)

def process_pvgis_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process the raw data from PVGIS API.
    
    Parameters:
    data (Dict[str, Any]): Raw data from PVGIS API
    
    Returns:
    Dict[str, Any]: Processed solar irradiance data
    """
    # Extract monthly averages
    monthly_data = data.get('outputs', {}).get('monthly', {})
    
    # Calculate average irradiance per month
    monthly_averages = []
    for month in monthly_data:
        # G_i_m is the average irradiance on the inclined plane (W/m²)
        monthly_averages.append(month.get('G_i_m', 0))
    
    # Calculate yearly average
    yearly_average = np.mean(monthly_averages)
    
    # Convert to peak sun hours (kWh/m²/day)
    peak_sun_hours = yearly_average / 1000  # Approximate conversion
    
    return {
        'monthly_averages': monthly_averages,
        'yearly_average': yearly_average,
        'peak_sun_hours': peak_sun_hours,
        'location': {
            'latitude': data.get('inputs', {}).get('location', {}).get('latitude', 0),
            'longitude': data.get('inputs', {}).get('location', {}).get('longitude', 0),
            'elevation': data.get('inputs', {}).get('location', {}).get('elevation', 0)
        }
    }

def simulate_kenya_irradiance_data(latitude: float, longitude: float) -> Dict[str, Any]:
    """
    Simulate solar irradiance data for Kenya when API is unavailable.
    
    Parameters:
    latitude (float): Latitude of the location
    longitude (float): Longitude of the location
    
    Returns:
    Dict[str, Any]: Simulated solar irradiance data
    """
    # Typical irradiance data for Kenya (monthly averages in W/m²)
    # These are approximate values and should be replaced with actual data
    kenya_monthly_averages = [
        620, 650, 630, 580, 540, 520, 540, 580, 620, 630, 610, 600  # Jan-Dec
    ]
    
    # Calculate yearly average
    yearly_average = np.mean(kenya_monthly_averages)
    
    # Convert to peak sun hours (kWh/m²/day)
    peak_sun_hours = yearly_average / 1000 * 8  # Approximate conversion
    
    return {
        'monthly_averages': kenya_monthly_averages,
        'yearly_average': yearly_average,
        'peak_sun_hours': peak_sun_hours,
        'location': {
            'latitude': latitude,
            'longitude': longitude,
            'elevation': 1000  # Default elevation
        },
        'simulated': True  # Flag to indicate this is simulated data
    }

def get_optimal_tilt_angle(latitude: float) -> float:
    """
    Calculate the optimal tilt angle for solar panels based on latitude.
    
    Parameters:
    latitude (float): Latitude of the location
    
    Returns:
    float: Optimal tilt angle for solar panels
    """
    # A simple approximation for optimal fixed tilt angle
    # For more accuracy, this would be calculated based on seasonal variations
    latitude_abs = abs(latitude)
    
    if latitude_abs < 10:
        # Near the equator
        return 10
    else:
        # Typical rule of thumb: latitude - 10° for hot climates
        return latitude_abs - 10
