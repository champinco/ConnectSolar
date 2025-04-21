import math
from typing import Dict, Any

def calculate_system_size(
    daily_energy_kwh: float,
    peak_sun_hours: float,
    panel_wattage: int = 400,
    battery_voltage: int = 24,
    battery_dod: float = 0.8,
    autonomy_days: int = 1,
    system_efficiency: float = 0.85,
    future_expansion: float = 0.2,
    max_panels: int = 50  # Added a max panels constraint for realistic residential systems
) -> Dict[str, Any]:
    """
    Calculate the recommended solar system size based on energy consumption and location.
    
    Parameters:
    daily_energy_kwh (float): Daily energy consumption in kWh
    peak_sun_hours (float): Peak sun hours for the location
    panel_wattage (int): Wattage of individual solar panels in W
    battery_voltage (int): Battery bank voltage in V
    battery_dod (float): Battery depth of discharge as a decimal (0.0-1.0)
    autonomy_days (int): Number of days of autonomy required
    system_efficiency (float): Overall system efficiency as a decimal (0.0-1.0)
    future_expansion (float): Future expansion factor as a decimal (0.0-1.0)
    max_panels (int): Maximum number of panels for a feasible residential system
    
    Returns:
    Dict[str, Any]: Dictionary containing calculated system parameters
    """
    # Apply a more balanced approach for efficiency and future expansion
    # Reducing their impact to make calculations more realistic
    adjusted_daily_energy = daily_energy_kwh * (1 + (future_expansion * 0.5)) / system_efficiency
    
    # Calculate panel array size (in kW)
    required_panel_output = adjusted_daily_energy / peak_sun_hours
    
    # Calculate number of panels needed
    panel_capacity_kw = panel_wattage / 1000  # Convert W to kW
    ideal_number_of_panels = math.ceil(required_panel_output / panel_capacity_kw)
    
    # Apply a cap on the number of panels to ensure feasibility
    number_of_panels = min(ideal_number_of_panels, max_panels)
    
    # Recalculate total panel capacity based on the adjusted panel number
    total_panel_capacity_kw = number_of_panels * panel_capacity_kw
    
    # Estimate what percentage of energy needs will be covered
    coverage_percentage = min(100, (total_panel_capacity_kw * peak_sun_hours * 100) / adjusted_daily_energy)
    
    # Estimate array area (assuming ~6 m² per kW of panels)
    # Most residential installations are 6-8 m² per kW, but we use a conservative 6 m²
    array_area_sqm = total_panel_capacity_kw * 6
    
    # Calculate battery capacity - ensure it's proportional to the actual panel capacity
    # If we can't fit all the panels, we should adjust battery capacity accordingly
    energy_produced = total_panel_capacity_kw * peak_sun_hours
    actual_coverage_ratio = min(1.0, energy_produced / adjusted_daily_energy)
    
    # Calculate battery capacity based on what can actually be produced
    battery_capacity_kwh = (adjusted_daily_energy * actual_coverage_ratio) * autonomy_days / battery_dod
    
    # Convert to Ah at the specified voltage
    battery_capacity_ah = battery_capacity_kwh * 1000 / battery_voltage
    
    # Return all calculated values including coverage percentage
    return {
        'daily_energy_kwh': daily_energy_kwh,
        'adjusted_daily_energy': adjusted_daily_energy,
        'peak_sun_hours': peak_sun_hours,
        'required_panel_output': required_panel_output,
        'panel_capacity_kw': panel_capacity_kw,
        'ideal_number_of_panels': ideal_number_of_panels,
        'number_of_panels': number_of_panels,
        'total_panel_capacity_kw': total_panel_capacity_kw,
        'coverage_percentage': coverage_percentage,
        'array_area_sqm': array_area_sqm,
        'battery_capacity_kwh': battery_capacity_kwh,
        'battery_capacity_ah': battery_capacity_ah,
        'battery_voltage': battery_voltage
    }

def calculate_inverter_size(panel_capacity_kw: float, ac_load_peak_kw: float = None) -> float:
    """
    Calculate the recommended inverter size based on panel capacity and AC loads.
    
    Parameters:
    panel_capacity_kw (float): Total solar panel capacity in kW
    ac_load_peak_kw (float, optional): Peak AC load in kW, if known
    
    Returns:
    float: Recommended inverter size in kW
    """
    # If AC load is provided, use the larger of AC load or panel capacity
    if ac_load_peak_kw:
        base_size = max(panel_capacity_kw, ac_load_peak_kw)
    else:
        base_size = panel_capacity_kw
    
    # Add 20% overhead for safety margin
    return base_size * 1.2

def calculate_wire_sizes(
    panel_capacity_kw: float,
    battery_voltage: int,
    distance_meters: Dict[str, float]
) -> Dict[str, Dict[str, Any]]:
    """
    Calculate recommended wire sizes for different parts of the solar system.
    
    Parameters:
    panel_capacity_kw (float): Total solar panel capacity in kW
    battery_voltage (int): Battery bank voltage
    distance_meters (Dict[str, float]): Dictionary with distances in meters for:
        - 'panel_to_controller': Distance from panels to charge controller
        - 'controller_to_battery': Distance from charge controller to batteries
        - 'battery_to_inverter': Distance from batteries to inverter
    
    Returns:
    Dict[str, Dict[str, Any]]: Recommended wire sizes for each connection
    """
    # Constants
    voltage_drop_allowance = 0.03  # 3% maximum voltage drop
    
    # Calculate current for different parts
    panel_current = (panel_capacity_kw * 1000) / battery_voltage  # Simplified calculation
    
    # Calculate wire sizes (this is a simplified calculation)
    wire_sizes = {}
    
    # Panel to charge controller
    panel_wire_size = calculate_wire_size(
        current=panel_current * 1.25,  # Add 25% for safety
        distance=distance_meters.get('panel_to_controller', 5),
        voltage=battery_voltage,
        voltage_drop=voltage_drop_allowance
    )
    wire_sizes['panel_to_controller'] = {
        'current': panel_current * 1.25,
        'distance': distance_meters.get('panel_to_controller', 5),
        'wire_size_mm2': panel_wire_size,
        'wire_size_awg': mm2_to_awg(panel_wire_size)
    }
    
    # Similar calculations for other connections...
    # In a real implementation, you would calculate sizes for all connections
    
    return wire_sizes

def calculate_wire_size(current: float, distance: float, voltage: float, voltage_drop: float) -> float:
    """
    Calculate wire cross-sectional area based on current, distance, and allowable voltage drop.
    
    Parameters:
    current (float): Current in amperes
    distance (float): Wire length in meters (one-way)
    voltage (float): System voltage
    voltage_drop (float): Allowable voltage drop as a decimal (e.g., 0.03 for 3%)
    
    Returns:
    float: Wire cross-sectional area in mm²
    """
    # Resistivity of copper in ohm·mm²/m
    resistivity = 0.0168
    
    # Calculate wire cross-sectional area
    area = (resistivity * current * distance * 2) / (voltage * voltage_drop)
    
    return area

def mm2_to_awg(mm2: float) -> int:
    """
    Convert wire size from mm² to AWG.
    
    Parameters:
    mm2 (float): Wire size in mm²
    
    Returns:
    int: Equivalent AWG size
    """
    # Approximate conversion formula
    if mm2 <= 0:
        return 0
    
    awg = -4.31 * math.log(mm2) + 36.2
    
    return round(awg)
