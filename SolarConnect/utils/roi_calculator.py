import numpy as np
from typing import Dict, List, Any

def calculate_grid_costs(
    annual_energy_kwh: float,
    energy_charge: float,
    fixed_charge: float,
    inflation_rate: float = 0.05,
    years: int = 25
) -> Dict[str, Any]:
    """
    Calculate the cost of grid electricity over a specified period.
    
    Parameters:
    annual_energy_kwh (float): Annual energy consumption in kWh
    energy_charge (float): Energy charge per kWh in KES
    fixed_charge (float): Fixed monthly charge in KES
    inflation_rate (float): Annual inflation rate for electricity costs
    years (int): Number of years to calculate costs for
    
    Returns:
    Dict[str, Any]: Dictionary containing grid electricity cost data
    """
    # Calculate base annual cost
    annual_energy_cost = annual_energy_kwh * energy_charge
    annual_fixed_cost = fixed_charge * 12
    base_annual_cost = annual_energy_cost + annual_fixed_cost
    
    # Calculate costs for each year with inflation
    annual_costs = []
    for year in range(years):
        year_cost = base_annual_cost * ((1 + inflation_rate) ** year)
        annual_costs.append(year_cost)
    
    # Calculate total cost over the period
    total_cost = sum(annual_costs)
    
    return {
        'annual_costs': annual_costs,
        'total_cost': total_cost,
        'base_annual_cost': base_annual_cost,
        'parameters': {
            'annual_energy_kwh': annual_energy_kwh,
            'energy_charge': energy_charge,
            'fixed_charge': fixed_charge,
            'inflation_rate': inflation_rate,
            'years': years
        }
    }

def calculate_roi(
    total_initial_cost: float,
    annual_maintenance: float,
    battery_replacement_cost: float,
    battery_replacement_years: int,
    grid_costs: Dict[str, Any],
    analysis_period: int = 25,
    financing_percentage: float = 0.7,  # Typical bank financing percentage
    financing_years: int = 7,  # Typical solar loan term
    financing_interest: float = 0.12  # Annual interest rate
) -> Dict[str, Any]:
    """
    Calculate return on investment for a solar system compared to grid electricity.
    
    Parameters:
    total_initial_cost (float): Total initial cost of the solar system in KES
    annual_maintenance (float): Annual maintenance cost in KES
    battery_replacement_cost (float): Cost to replace batteries in KES
    battery_replacement_years (int): Years between battery replacements
    grid_costs (Dict[str, Any]): Grid cost data from calculate_grid_costs()
    analysis_period (int): Number of years for the analysis
    financing_percentage (float): Percentage of system cost that's financed (0.0-1.0)
    financing_years (int): Years over which financing is spread
    financing_interest (float): Annual interest rate on financing
    
    Returns:
    Dict[str, Any]: Dictionary containing ROI analysis data
    """
    # Get annual grid costs
    grid_annual_costs = grid_costs['annual_costs']
    
    # Calculate financing
    financed_amount = total_initial_cost * financing_percentage
    down_payment = total_initial_cost - financed_amount
    
    # Calculate annual loan payment using PMT formula (principal + interest)
    monthly_rate = financing_interest / 12
    total_payments = financing_years * 12
    monthly_payment = (financed_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -total_payments)
    annual_loan_payment = monthly_payment * 12
    
    # Calculate annual solar costs - spreading initial cost over financing period
    solar_annual_costs = []
    
    # First year includes down payment and loan payments
    solar_annual_costs.append(down_payment + annual_maintenance + annual_loan_payment)
    
    # Subsequent years
    for year in range(1, analysis_period):
        year_cost = annual_maintenance
        
        # Add loan payment if still in financing period
        if year < financing_years:
            year_cost += annual_loan_payment
            
        # Add battery replacement cost if needed
        if year % battery_replacement_years == 0:
            year_cost += battery_replacement_cost
        
        solar_annual_costs.append(year_cost)
    
    # Calculate cumulative costs
    grid_cumulative = np.cumsum(grid_annual_costs)
    solar_cumulative = np.cumsum(solar_annual_costs)
    
    # Calculate annual savings (can be positive from year 1 with financing)
    annual_savings = []
    for i in range(analysis_period):
        annual_savings.append(grid_annual_costs[i] - solar_annual_costs[i])
    
    # Calculate cumulative savings
    cumulative_savings = []
    for i in range(analysis_period):
        cumulative_savings.append(grid_cumulative[i] - solar_cumulative[i])
    
    # Calculate payback period
    payback_period = calculate_payback_period(solar_cumulative, grid_cumulative)
    
    # Calculate ROI percentage
    if analysis_period < len(cumulative_savings):
        total_savings = cumulative_savings[analysis_period - 1]
    else:
        total_savings = cumulative_savings[-1]
    
    roi_percent = (total_savings / total_initial_cost) * 100
    
    # Calculate first-year savings
    first_year_savings = annual_savings[0] if annual_savings else 0
    first_year_savings_percentage = (first_year_savings / grid_annual_costs[0]) * 100 if grid_annual_costs else 0
    
    # Calculate average monthly savings in first year
    monthly_first_year_savings = first_year_savings / 12 if first_year_savings else 0
    
    return {
        'payback_period': payback_period,
        'roi_percent': roi_percent,
        'total_savings': total_savings,
        'annual_savings': annual_savings,
        'cumulative_savings': cumulative_savings,
        'solar_annual_costs': solar_annual_costs,
        'solar_cumulative_costs': solar_cumulative.tolist(),
        'grid_cumulative_costs': grid_cumulative.tolist(),
        'first_year_savings': first_year_savings,
        'first_year_savings_percentage': first_year_savings_percentage,
        'monthly_first_year_savings': monthly_first_year_savings,
        'financing_details': {
            'down_payment': down_payment,
            'financed_amount': financed_amount,
            'monthly_payment': monthly_payment,
            'annual_payment': annual_loan_payment,
            'financing_years': financing_years,
            'interest_rate': financing_interest
        }
    }

def calculate_payback_period(solar_cumulative: np.array, grid_cumulative: np.array) -> float:
    """
    Calculate the payback period by finding when cumulative grid costs exceed solar costs.
    
    Parameters:
    solar_cumulative (np.array): Cumulative solar costs
    grid_cumulative (np.array): Cumulative grid costs
    
    Returns:
    float: Payback period in years
    """
    # Find the point where grid costs exceed solar costs
    for i in range(1, len(solar_cumulative)):
        if grid_cumulative[i] > solar_cumulative[i]:
            # Linear interpolation for more accurate payback period
            prev_diff = solar_cumulative[i-1] - grid_cumulative[i-1]
            curr_diff = solar_cumulative[i] - grid_cumulative[i]
            
            # If curr_diff is positive, we haven't reached break-even yet
            if curr_diff >= 0:
                continue
            
            # Calculate the fractional year where break-even occurs
            fraction = prev_diff / (prev_diff - curr_diff)
            return i - 1 + fraction
    
    # If no break-even point is found, return a value larger than the analysis period
    return len(solar_cumulative) + 1
