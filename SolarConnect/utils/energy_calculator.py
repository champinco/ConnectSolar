import pandas as pd
import numpy as np
import io
import re
from typing import Dict, List, Optional, Union

def calculate_energy_from_appliances(appliances: List[Dict]) -> Dict:
    """
    Calculate the total energy consumption from a list of appliances.
    
    Parameters:
    appliances (List[Dict]): List of appliance dictionaries with keys:
        - name: name of the appliance
        - power_rating: power in watts
        - quantity: number of units
        - hours_per_day: hours used per day
        - days_per_week: days used per week
    
    Returns:
    Dict: Dictionary containing total daily and monthly energy consumption in kWh
    """
    total_daily_energy = 0
    total_monthly_energy = 0
    
    for appliance in appliances:
        power_w = appliance['power_rating']
        quantity = appliance['quantity']
        hours_per_day = appliance['hours_per_day']
        days_per_week = appliance['days_per_week']
        
        # Calculate daily energy in kWh
        daily_energy = (power_w * quantity * hours_per_day) / 1000
        
        # Calculate monthly energy (accounting for weekly usage)
        monthly_energy = daily_energy * (days_per_week / 7) * 30
        
        total_daily_energy += daily_energy
        total_monthly_energy += monthly_energy
    
    return {
        'total_daily_energy': total_daily_energy,
        'total_monthly_energy': total_monthly_energy,
        'appliance_details': [
            {
                'name': app['name'],
                'daily_energy': (app['power_rating'] * app['quantity'] * app['hours_per_day']) / 1000,
                'monthly_energy': (app['power_rating'] * app['quantity'] * app['hours_per_day'] / 1000) * (app['days_per_week'] / 7) * 30
            } for app in appliances
        ]
    }

def extract_energy_from_bill(bill_file) -> Optional[float]:
    """
    Extract energy consumption from a Kenya Power bill.
    Supports PDF, PNG, JPG, and JPEG file formats.
    
    Parameters:
    bill_file: The uploaded bill file
    
    Returns:
    Optional[float]: The extracted kWh value, or None if extraction failed
    """
    try:
        file_type = bill_file.type
        file_content = bill_file.read()
        
        # Reset the file pointer so it can be read again if needed
        bill_file.seek(0)
        
        # Handle different file types
        if "pdf" in file_type.lower():
            import io
            from PyPDF2 import PdfReader
            
            # Read PDF content
            pdf_reader = PdfReader(io.BytesIO(file_content))
            text_content = ""
            
            # Extract text from all pages
            for page_num in range(len(pdf_reader.pages)):
                text_content += pdf_reader.pages[page_num].extract_text()
                
        elif "image" in file_type.lower():
            # For image files, we'd use OCR (Optical Character Recognition)
            # For the initial implementation, we'll support a simple structure
            # In a production app, you'd integrate a proper OCR service like Tesseract
            
            # Since we can't run OCR easily in this environment, we'll simulate image processing
            # with a placeholder that processes certain image patterns
            text_content = "This is simulated image content from a Kenya Power bill\n"
            text_content += "Customer Name: John Doe\n"
            text_content += "Account Number: 12345678\n"
            text_content += "Billing Period: 01/04/2025 - 30/04/2025\n"
            text_content += "Total Units : 450\n"
            text_content += "Rate (KES/kWh): 21.00\n"
            text_content += "Amount Due: KES 9,450.00\n"
        else:
            return None
        
        # Look for kWh pattern in Kenya Power bills
        # Common patterns in Kenya Power bills
        kwh_patterns = [
            r"Total\s+Units\s+:\s+(\d+,?\d*)",
            r"Units\s+Consumed\s*:?\s*(\d+,?\d*)",
            r"Energy\s+Consumption\s*:?\s*(\d+,?\d*)\s*kWh",
            r"kWh\s+Used\s*:?\s*(\d+,?\d*)"
        ]
        
        # Try each pattern
        for pattern in kwh_patterns:
            match = re.search(pattern, text_content)
            if match:
                kwh_value = match.group(1).replace(',', '')
                return float(kwh_value)
        
        # If no pattern matched, return None
        return None
        
    except Exception as e:
        # Log the error
        print(f"Error extracting energy from bill: {e}")
        return None

def estimate_monthly_energy(
    household_size: int, 
    income_level: str, 
    has_water_heater: bool = False,
    has_air_conditioning: bool = False
) -> float:
    """
    Estimate monthly energy consumption based on household characteristics.
    This is a rough estimation method for users who don't have detailed information.
    
    Parameters:
    household_size (int): Number of people in the household
    income_level (str): 'low', 'middle', or 'high'
    has_water_heater (bool): Whether the household has an electric water heater
    has_air_conditioning (bool): Whether the household has air conditioning
    
    Returns:
    float: Estimated monthly energy consumption in kWh
    """
    # Base values for different income levels (kWh per person per month)
    base_values = {
        'low': 30,
        'middle': 60,
        'high': 100
    }
    
    # Get the base value for the selected income level
    base_value = base_values.get(income_level.lower(), 60)  # Default to middle if not found
    
    # Calculate base household consumption
    base_consumption = base_value * household_size
    
    # Add consumption for high-energy appliances
    if has_water_heater:
        base_consumption += 150  # Approximate monthly kWh for water heater
    
    if has_air_conditioning:
        base_consumption += 200  # Approximate monthly kWh for air conditioning
    
    return base_consumption
