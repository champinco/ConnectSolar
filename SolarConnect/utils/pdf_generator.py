import io
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Any
import base64

def generate_pdf_report(data: Dict[str, Any]) -> bytes:
    """
    Generate a PDF report with solar system details, cost analysis, and ROI.
    
    Parameters:
    data (Dict[str, Any]): Dictionary containing all data for the report
    
    Returns:
    bytes: PDF report as bytes
    """
    # Create a file-like buffer to receive PDF data
    buffer = io.BytesIO()
    
    # Create the PDF object
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    
    # Container for the elements to be added to the PDF
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    title_style = styles['Heading1']
    subtitle_style = styles['Heading2']
    normal_style = styles['Normal']
    
    # Create custom styles
    section_title_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        spaceBefore=10,
        spaceAfter=6,
        textColor=colors.darkorange
    )
    
    # Add title
    elements.append(Paragraph("Solar System Report", title_style))
    elements.append(Spacer(1, 0.25*inch))
    
    # Add customer information
    elements.append(Paragraph("Customer Information", section_title_style))
    customer_info = [
        ["Name:", data['customer_info']['name']],
        ["Email:", data['customer_info']['email']],
        ["Phone:", data['customer_info']['phone']],
        ["Date:", data['customer_info']['date']]
    ]
    t = Table(customer_info, colWidths=[1.5*inch, 4*inch])
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.25*inch))
    
    # Add location information
    if 'location' in data:
        elements.append(Paragraph("Location", section_title_style))
        location_info = [
            ["Location:", data['location']['location_name']],
            ["Latitude:", f"{data['location']['latitude']:.6f}"],
            ["Longitude:", f"{data['location']['longitude']:.6f}"]
        ]
        t = Table(location_info, colWidths=[1.5*inch, 4*inch])
        t.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        elements.append(t)
        elements.append(Spacer(1, 0.25*inch))
    
    # Add energy usage information
    elements.append(Paragraph("Energy Consumption", section_title_style))
    energy_info = [
        ["Daily Energy Consumption:", f"{data['energy_usage']['daily_kwh']:.2f} kWh"],
        ["Monthly Energy Consumption:", f"{data['energy_usage']['monthly_kwh']:.2f} kWh"],
        ["Annual Energy Consumption:", f"{data['energy_usage']['monthly_kwh'] * 12:.2f} kWh"]
    ]
    t = Table(energy_info, colWidths=[2*inch, 3.5*inch])
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.25*inch))
    
    # Add solar system details
    elements.append(Paragraph("Recommended Solar System", section_title_style))
    solar_info = [
        ["Solar Array Size:", f"{data['solar_sizing']['total_panel_capacity_kw']:.2f} kWp"],
        ["Number of Panels:", f"{data['solar_sizing']['number_of_panels']}"],
        ["Battery Capacity:", f"{data['solar_sizing']['battery_capacity_kwh']:.2f} kWh"],
        ["Battery Voltage:", f"{data['solar_sizing']['battery_voltage']} V"],
        ["Array Area (approx.):", f"{data['solar_sizing']['array_area_sqm']:.2f} m²"]
    ]
    t = Table(solar_info, colWidths=[2*inch, 3.5*inch])
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.25*inch))
    
    # Add cost analysis
    elements.append(Paragraph("Cost Analysis", section_title_style))
    cost_info = [
        ["Initial Investment:", f"KES {data['cost_analysis']['total_initial_cost']:,.2f}"],
        ["Solar Panels:", f"KES {data['cost_analysis']['panel_cost']:,.2f}"],
        ["Battery System:", f"KES {data['cost_analysis']['battery_cost']:,.2f}"],
        ["Inverter:", f"KES {data['cost_analysis']['inverter_cost']:,.2f}"],
        ["Installation:", f"KES {data['cost_analysis']['installation_cost']:,.2f}"],
        ["Annual Maintenance:", f"KES {data['cost_analysis']['maintenance_annual']:,.2f}"]
    ]
    t = Table(cost_info, colWidths=[2*inch, 3.5*inch])
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.25*inch))
    
    # Add ROI analysis
    elements.append(Paragraph("Return on Investment", section_title_style))
    roi_info = [
        ["Payback Period:", f"{data['roi_data']['payback_period']:.1f} years"],
        ["ROI:", f"{data['roi_data']['roi_percent']:.1f}%"],
        ["Lifetime Savings:", f"KES {data['roi_data']['total_savings']:,.2f}"],
        ["Analysis Period:", f"{data['cost_analysis']['analysis_period']} years"]
    ]
    t = Table(roi_info, colWidths=[2*inch, 3.5*inch])
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.25*inch))
    
    # Generate cost comparison chart
    fig, ax = plt.subplots(figsize=(7, 4))
    years = list(range(1, data['cost_analysis']['analysis_period'] + 1))
    
    # Extract cumulative costs
    grid_costs = data['roi_data']['grid_cumulative_costs']
    solar_costs = data['roi_data']['solar_cumulative_costs']
    
    # Plot cumulative costs
    ax.plot(years, grid_costs, 'b-', label='Grid Electricity')
    ax.plot(years, solar_costs, 'g-', label='Solar System')
    
    # Mark the payback point
    payback_period = data['roi_data']['payback_period']
    if payback_period <= data['cost_analysis']['analysis_period']:
        # Find the approximate cost at payback point
        payback_year = int(payback_period)
        payback_fraction = payback_period - payback_year
        
        if payback_year < len(solar_costs):
            if payback_year > 0:
                payback_cost = solar_costs[payback_year-1] + (solar_costs[payback_year] - solar_costs[payback_year-1]) * payback_fraction
            else:
                payback_cost = solar_costs[0] * payback_fraction
            
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
    
    # Save the figure to a buffer
    chart_buffer = io.BytesIO()
    plt.savefig(chart_buffer, format='png')
    chart_buffer.seek(0)
    
    # Add the chart to the PDF
    elements.append(Paragraph("Cost Comparison Chart", section_title_style))
    img = Image(chart_buffer, width=6*inch, height=3.5*inch)
    elements.append(img)
    elements.append(Spacer(1, 0.25*inch))
    
    # Generate disclaimer text
    elements.append(Paragraph("Disclaimer", section_title_style))
    disclaimer_text = """
    This report provides an estimate based on the information provided and general assumptions. 
    Actual costs, savings, and payback period may vary depending on specific installation 
    conditions, equipment used, and future electricity prices. It is recommended to consult 
    with qualified solar professionals before making any investment decisions.
    """
    elements.append(Paragraph(disclaimer_text, normal_style))
    elements.append(Spacer(1, 0.25*inch))
    
    # Closing message
    elements.append(Paragraph("Next Steps", section_title_style))
    next_steps = """
    1. Contact qualified solar installers for a detailed assessment and quotation.
    2. Verify available space for panel installation at your property.
    3. Check for any local permits or regulations that may apply to solar installations.
    4. Inquire about available incentives or financing options for solar systems.
    
    Thank you for using the Kenya Solar System Sizing App!
    """
    elements.append(Paragraph(next_steps, normal_style))
    
    # Build the PDF
    doc.build(elements)
    
    # Get the PDF value from the buffer and return it
    buffer.seek(0)
    return buffer.getvalue()
