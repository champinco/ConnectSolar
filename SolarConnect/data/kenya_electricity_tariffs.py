def get_electricity_tariff(consumer_type):
    """
    Get the current electricity tariff information for Kenya.
    
    Parameters:
    consumer_type (str): The type of consumer (Domestic, Small Commercial, Commercial, or Industrial)
    
    Returns:
    dict: Dictionary containing tariff information
    """
    # Kenya Power tariff information (as of mid-2023)
    # These rates should be updated periodically to reflect current tariffs
    tariffs = {
        "Domestic": {
            "category": "Domestic (DC)",
            "energy_charge": "21.00",  # KES per kWh
            "fixed_charge": "200",     # KES per month
            "description": "For domestic consumers with single phase supply"
        },
        "Small Commercial": {
            "category": "Small Commercial (SC)",
            "energy_charge": "22.70",  # KES per kWh
            "fixed_charge": "250",     # KES per month
            "description": "For small commercial consumers with single phase supply"
        },
        "Commercial (DC)": {
            "category": "Commercial (DC)",
            "energy_charge": "23.50",  # KES per kWh
            "fixed_charge": "3500",    # KES per month
            "description": "For commercial consumers with three phase supply"
        },
        "Industrial": {
            "category": "Industrial (IT)",
            "energy_charge": "20.60",  # KES per kWh
            "fixed_charge": "4500",    # KES per month
            "description": "For industrial consumers with high power requirements"
        }
    }
    
    # Return the tariff information for the specified consumer type
    if consumer_type in tariffs:
        return tariffs[consumer_type]
    else:
        # Return domestic tariff as default
        return tariffs["Domestic"]
