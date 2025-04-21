# Comprehensive dictionary of appliances organized by category with their typical power ratings in watts
appliance_categories = {
    "Residential": {
        "Lighting": {
            "LED Light Bulb": 10,
            "CFL Light Bulb": 20,
            "Incandescent Light Bulb": 60,
            "LED Tube Light": 18,
            "LED Downlight": 12,
            "Bedside Lamp": 40,
            "Security Light (Outdoor)": 25,
            "Motion Sensor Light": 20,
            "Garden Lights": 10,
            "Decorative String Lights": 15
        },
        "Cooling & Heating": {
            "Ceiling Fan": 75,
            "Standing Fan": 50,
            "Table Fan": 40,
            "Wall Fan": 60,
            "Air Conditioner (1 ton)": 1000,
            "Air Conditioner (1.5 ton)": 1500,
            "Air Conditioner (2 ton)": 2000,
            "Portable Air Cooler": 80,
            "Space Heater": 1500,
            "Room Heater": 1200
        },
        "Kitchen": {
            "Refrigerator (Small)": 100,
            "Refrigerator (Medium)": 150,
            "Refrigerator (Large)": 200,
            "Chest Freezer": 200,
            "Microwave Oven": 1200,
            "Electric Kettle": 1500,
            "Electric Water Dispenser": 500,
            "Toaster": 850,
            "Coffee Maker": 800,
            "Blender": 400,
            "Food Processor": 500,
            "Juicer": 300,
            "Electric Rice Cooker": 700,
            "Electric Pressure Cooker": 1000,
            "Electric Oven": 2000,
            "Electric Stove (single burner)": 1500,
            "Electric Stove (double burner)": 3000,
            "Mixer Grinder": 750,
            "Dishwasher": 1500,
            "Water Purifier": 50
        },
        "Entertainment & Electronics": {
            "Television (24\" LED)": 40,
            "Television (32\" LED)": 50,
            "Television (42\" LED)": 80,
            "Television (55\" LED)": 120,
            "DVD/Blu-ray Player": 25,
            "Set-top Box/Decoder": 30,
            "Video Game Console": 150,
            "Sound System/Home Theater": 100,
            "Stereo System": 80,
            "Radio": 20,
            "Smart Speaker": 10,
            "Media Streaming Device": 5
        },
        "Computing & Communications": {
            "Wi-Fi Router": 10,
            "Internet Modem": 10,
            "Mobile Phone Charger": 5,
            "Tablet Charger": 10,
            "Laptop Computer": 65,
            "Desktop Computer": 150,
            "Computer Monitor": 80,
            "Printer (Inkjet)": 30,
            "Printer (Laser)": 400,
            "Scanner": 15,
            "External Hard Drive": 10,
            "UPS Backup System": 300
        },
        "Laundry & Bathroom": {
            "Washing Machine": 500,
            "Clothes Dryer": 3000,
            "Electric Iron": 1000,
            "Electric Hair Dryer": 1500,
            "Electric Shaver": 15,
            "Electric Toothbrush Charger": 5,
            "Electric Water Heater (Storage)": 3000,
            "Instant Water Heater": 4000,
            "Bathroom Exhaust Fan": 25
        },
        "Home Maintenance": {
            "Vacuum Cleaner": 800,
            "Electric Broom": 200,
            "Electric Mop": 150,
            "Clothes Iron": 1000,
            "Sewing Machine": 100,
            "Electric Pump (0.5 HP)": 375,
            "Electric Water Pump (1 HP)": 750,
            "Borehole Pump (1 HP)": 750,
            "Electric Lawn Mower": 1200,
            "Electric Hedge Trimmer": 500
        },
        "Security & Safety": {
            "Security Camera": 15,
            "CCTV System (4 cameras)": 50,
            "Video Doorbell": 5,
            "Electric Gate Motor": 300,
            "Electric Fence": 10,
            "Alarm System": 5,
            "Motion Sensors": 1
        }
    },
    "Commercial": {
        "Office Equipment": {
            "Desktop Computer": 150,
            "Laptop Computer": 65,
            "Server Computer": 350,
            "Network Switch": 50,
            "Laser Printer": 400,
            "Multifunction Printer": 500,
            "Photocopier": 1500,
            "Scanner": 15,
            "Shredder": 200,
            "Projector": 300,
            "Digital Display Screen": 120,
            "TV for Reception": 80,
            "Cash Register": 50,
            "Barcode Scanner": 10,
            "Credit Card Terminal": 8
        },
        "Office Comfort": {
            "Air Conditioner (Office)": 2500,
            "Standing Fan": 50,
            "Ceiling Fan": 75,
            "Air Purifier": 80,
            "Water Dispenser": 500,
            "Coffee Machine (Commercial)": 1500,
            "Microwave": 1200,
            "Small Refrigerator": 120,
            "Vending Machine": 800
        },
        "Lighting": {
            "Fluorescent Tube Light (4ft)": 40,
            "LED Panel Light": 45,
            "Office Downlights": 15,
            "Signage Lighting": 100,
            "Emergency Exit Lights": 5,
            "Outdoor Security Lights": 50
        },
        "Retail": {
            "Display Refrigerator": 450,
            "Freezer Display": 500,
            "POS System": 150,
            "Barcode Scanner": 10,
            "Electronic Scale": 10,
            "CCTV System": 100,
            "Anti-theft Security Gate": 50,
            "Digital Signage": 150
        },
        "Food Service": {
            "Commercial Refrigerator": 800,
            "Commercial Freezer": 1200,
            "Ice Machine": 500,
            "Blender (Commercial)": 1000,
            "Coffee Machine": 1800,
            "Food Warmer": 1500,
            "Electric Grill": 2000,
            "Deep Fryer": 3000,
            "Microwave (Commercial)": 1800,
            "Toaster (Commercial)": 1500,
            "Commercial Dishwasher": 2000,
            "Pizza Oven": 5000,
            "Exhaust Hood": 550
        },
        "Salon & Spa": {
            "Hair Dryer": 1500,
            "Hair Straightener": 120,
            "Hair Curler": 100,
            "Nail Dryer": 36,
            "Electric Massage Chair": 200,
            "Facial Steamer": 650,
            "Hot Towel Cabinet": 200,
            "Salon Chair Lift": 200
        }
    },
    "Industrial": {
        "Manufacturing": {
            "Small Electric Motor (0.5 HP)": 375,
            "Medium Electric Motor (1 HP)": 750,
            "Large Electric Motor (5 HP)": 3730,
            "Industrial Fan": 750,
            "Air Compressor (Small)": 1500,
            "Air Compressor (Medium)": 3700,
            "Air Compressor (Large)": 7500,
            "Industrial Pump": 2200,
            "Conveyor Belt System": 1500,
            "Hydraulic Press": 5500,
            "Welding Machine": 5000,
            "CNC Machine": 4000,
            "Lathe Machine": 1500,
            "Injection Molding Machine": 10000,
            "Industrial Oven": 5000,
            "Industrial Mixer": 3000,
            "Industrial Grinder": 2500
        },
        "Warehouse": {
            "Forklift Charger": 3000,
            "Pallet Jack Charger": 500,
            "Industrial Lighting (per fixture)": 250,
            "Loading Dock Equipment": 1500,
            "Conveyor System": 2000,
            "Packaging Machine": 1500,
            "Shrink Wrap Machine": 1200,
            "Industrial Scale": 200,
            "Barcode Printer": 300
        },
        "Commercial Cooling": {
            "Walk-in Refrigerator": 2000,
            "Walk-in Freezer": 3500,
            "Cold Storage Compressor": 5000,
            "Industrial Air Conditioner (5 ton)": 5000,
            "Cooling Tower": 3500,
            "Industrial Chiller": 8000
        },
        "Water Systems": {
            "Water Treatment Pump": 1100,
            "Borehole Pump (3 HP)": 2250,
            "Borehole Pump (5 HP)": 3730,
            "Water Filtration System": 500,
            "Irrigation Pump": 1500,
            "Pressure Booster Pump": 1100
        }
    },
    "Agricultural": {
        "Irrigation": {
            "Water Pump (1 HP)": 750,
            "Water Pump (2 HP)": 1500,
            "Drip Irrigation Controller": 50,
            "Sprinkler System Controller": 50,
            "Irrigation Timer": 10
        },
        "Livestock": {
            "Milk Cooler": 1500,
            "Milking Machine": 1100,
            "Incubator": 200,
            "Animal Feed Grinder": 1500,
            "Feed Mixer": 1100,
            "Water Heater (Livestock)": 3000,
            "Heat Lamp": 250
        },
        "Processing": {
            "Grain Mill": 2200,
            "Grain Dryer": 5000,
            "Coffee Pulper": 750,
            "Sugar Cane Crusher": 1500,
            "Fruit Pulper": 750,
            "Oil Press": 1500
        },
        "Storage": {
            "Cold Storage Room": 2500,
            "Grain Aerator": 750,
            "Greenhouse Fan": 500,
            "Greenhouse Heater": 1500,
            "Humidity Controller": 100
        }
    },
    "Healthcare": {
        "Medical Equipment": {
            "Refrigerator (Vaccines)": 200,
            "Ultrasound Machine": 1000,
            "ECG Machine": 300,
            "X-Ray Machine": 4000,
            "Dental Chair": 900,
            "Sterilizer": 1500,
            "Patient Monitor": 150,
            "Oxygen Concentrator": 350,
            "Nebulizer": 80,
            "Suction Machine": 150,
            "Electric Hospital Bed": 200
        },
        "Laboratory": {
            "Centrifuge": 300,
            "Microscope": 30,
            "Laboratory Refrigerator": 300,
            "Laboratory Freezer": 400,
            "Autoclave": 1800,
            "Lab Incubator": 400,
            "Water Bath": 1200,
            "Magnetic Stirrer": 50,
            "Laboratory Shaker": 150
        }
    },
    "Educational": {
        "Classroom": {
            "Projector": 300,
            "Interactive Whiteboard": 100,
            "Computer Lab (per computer)": 200,
            "Printer Room": 600,
            "Air Conditioner (Classroom)": 1500,
            "Ceiling Fan": 75,
            "PA System": 100,
            "Document Camera": 50,
            "Smart Board": 200
        },
        "Administrative": {
            "Server Room": 2000,
            "Security System": 200,
            "Bell System": 100,
            "Library Equipment": 500,
            "Photocopier Room": 1500,
            "Staff Room Equipment": 800
        },
        "Facilities": {
            "Water Pump": 750,
            "Kitchen Equipment": 4000,
            "Science Lab Equipment": 1500,
            "Computer Lab": 3000,
            "Gymnasium Equipment": 1000
        }
    }
}

# Flatten the nested structure for easy lookup
common_appliances = {}
for category in appliance_categories:
    for subcategory in appliance_categories[category]:
        for appliance, power in appliance_categories[category][subcategory].items():
            common_appliances[appliance] = power

# Expanded appliance groups for quick selection
appliance_groups = {
    "Basic Lighting": [
        {"name": "LED Light Bulb", "quantity": 6, "hours_per_day": 5, "days_per_week": 7},
        {"name": "Mobile Phone Charger", "quantity": 2, "hours_per_day": 2, "days_per_week": 7},
        {"name": "Television (32\" LED)", "quantity": 1, "hours_per_day": 4, "days_per_week": 7},
        {"name": "Wi-Fi Router", "quantity": 1, "hours_per_day": 24, "days_per_week": 7}
    ],
    "Small Home": [
        {"name": "LED Light Bulb", "quantity": 8, "hours_per_day": 5, "days_per_week": 7},
        {"name": "Ceiling Fan", "quantity": 2, "hours_per_day": 8, "days_per_week": 7},
        {"name": "Television (32\" LED)", "quantity": 1, "hours_per_day": 6, "days_per_week": 7},
        {"name": "Refrigerator (Small)", "quantity": 1, "hours_per_day": 24, "days_per_week": 7},
        {"name": "Mobile Phone Charger", "quantity": 3, "hours_per_day": 3, "days_per_week": 7},
        {"name": "Laptop Computer", "quantity": 1, "hours_per_day": 4, "days_per_week": 5},
        {"name": "Wi-Fi Router", "quantity": 1, "hours_per_day": 24, "days_per_week": 7}
    ],
    "Medium Home": [
        {"name": "LED Light Bulb", "quantity": 12, "hours_per_day": 6, "days_per_week": 7},
        {"name": "Ceiling Fan", "quantity": 3, "hours_per_day": 10, "days_per_week": 7},
        {"name": "Television (42\" LED)", "quantity": 1, "hours_per_day": 6, "days_per_week": 7},
        {"name": "Refrigerator (Medium)", "quantity": 1, "hours_per_day": 24, "days_per_week": 7},
        {"name": "Mobile Phone Charger", "quantity": 4, "hours_per_day": 3, "days_per_week": 7},
        {"name": "Laptop Computer", "quantity": 2, "hours_per_day": 6, "days_per_week": 7},
        {"name": "Wi-Fi Router", "quantity": 1, "hours_per_day": 24, "days_per_week": 7},
        {"name": "Microwave Oven", "quantity": 1, "hours_per_day": 0.5, "days_per_week": 7},
        {"name": "Electric Iron", "quantity": 1, "hours_per_day": 0.5, "days_per_week": 3}
    ],
    "Large Home": [
        {"name": "LED Light Bulb", "quantity": 20, "hours_per_day": 6, "days_per_week": 7},
        {"name": "Ceiling Fan", "quantity": 5, "hours_per_day": 10, "days_per_week": 7},
        {"name": "Television (55\" LED)", "quantity": 2, "hours_per_day": 6, "days_per_week": 7},
        {"name": "Refrigerator (Large)", "quantity": 1, "hours_per_day": 24, "days_per_week": 7},
        {"name": "Chest Freezer", "quantity": 1, "hours_per_day": 24, "days_per_week": 7},
        {"name": "Mobile Phone Charger", "quantity": 6, "hours_per_day": 3, "days_per_week": 7},
        {"name": "Laptop Computer", "quantity": 3, "hours_per_day": 6, "days_per_week": 7},
        {"name": "Wi-Fi Router", "quantity": 1, "hours_per_day": 24, "days_per_week": 7},
        {"name": "Microwave Oven", "quantity": 1, "hours_per_day": 1, "days_per_week": 7},
        {"name": "Electric Kettle", "quantity": 1, "hours_per_day": 0.5, "days_per_week": 7},
        {"name": "Washing Machine", "quantity": 1, "hours_per_day": 1, "days_per_week": 3},
        {"name": "Air Conditioner (1.5 ton)", "quantity": 2, "hours_per_day": 6, "days_per_week": 7},
        {"name": "Water Pump (1 HP)", "quantity": 1, "hours_per_day": 2, "days_per_week": 7}
    ],
    "Small Office": [
        {"name": "LED Light Bulb", "quantity": 10, "hours_per_day": 9, "days_per_week": 5},
        {"name": "Ceiling Fan", "quantity": 3, "hours_per_day": 9, "days_per_week": 5},
        {"name": "Desktop Computer", "quantity": 3, "hours_per_day": 8, "days_per_week": 5},
        {"name": "Laser Printer", "quantity": 1, "hours_per_day": 2, "days_per_week": 5},
        {"name": "Wi-Fi Router", "quantity": 1, "hours_per_day": 24, "days_per_week": 7},
        {"name": "Small Refrigerator", "quantity": 1, "hours_per_day": 24, "days_per_week": 7},
        {"name": "Microwave", "quantity": 1, "hours_per_day": 0.5, "days_per_week": 5},
        {"name": "Water Dispenser", "quantity": 1, "hours_per_day": 9, "days_per_week": 5}
    ],
    "Small Shop": [
        {"name": "LED Light Bulb", "quantity": 8, "hours_per_day": 12, "days_per_week": 6},
        {"name": "Ceiling Fan", "quantity": 2, "hours_per_day": 12, "days_per_week": 6},
        {"name": "Refrigerator (Medium)", "quantity": 1, "hours_per_day": 24, "days_per_week": 7},
        {"name": "Cash Register", "quantity": 1, "hours_per_day": 12, "days_per_week": 6},
        {"name": "Security Camera", "quantity": 2, "hours_per_day": 24, "days_per_week": 7},
        {"name": "Television (32\" LED)", "quantity": 1, "hours_per_day": 12, "days_per_week": 6}
    ],
    "Small Restaurant": [
        {"name": "LED Light Bulb", "quantity": 10, "hours_per_day": 12, "days_per_week": 7},
        {"name": "Ceiling Fan", "quantity": 4, "hours_per_day": 12, "days_per_week": 7},
        {"name": "Commercial Refrigerator", "quantity": 1, "hours_per_day": 24, "days_per_week": 7},
        {"name": "Deep Freezer", "quantity": 1, "hours_per_day": 24, "days_per_week": 7},
        {"name": "Blender (Commercial)", "quantity": 1, "hours_per_day": 2, "days_per_week": 7},
        {"name": "Microwave (Commercial)", "quantity": 1, "hours_per_day": 3, "days_per_week": 7},
        {"name": "Electric Grill", "quantity": 1, "hours_per_day": 6, "days_per_week": 7},
        {"name": "Coffee Machine", "quantity": 1, "hours_per_day": 8, "days_per_week": 7},
        {"name": "Cash Register", "quantity": 1, "hours_per_day": 12, "days_per_week": 7},
        {"name": "Television (42\" LED)", "quantity": 1, "hours_per_day": 12, "days_per_week": 7},
        {"name": "Security Camera", "quantity": 3, "hours_per_day": 24, "days_per_week": 7}
    ]
}

def get_common_appliances():
    """Return the dictionary of common appliances with their power ratings"""
    return common_appliances

def get_appliance_categories():
    """Return the categorized dictionary of appliances with their power ratings"""
    return appliance_categories

def get_appliance_groups():
    """Return predefined appliance groups for quick selection"""
    return appliance_groups
