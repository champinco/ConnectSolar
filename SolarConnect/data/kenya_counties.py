"""
Kenya Counties Data Module

This module provides geographical and climate data for all 47 counties in Kenya.
Includes coordinates, elevation, peak sun hours, temperatures, and administrative information.
"""

def get_kenya_counties():
    """
    Return a comprehensive dictionary with data for all 47 counties in Kenya.
    
    Returns:
    dict: Dictionary with county data including coordinates, climate data, etc.
    """
    counties = {
        "Mombasa": {
            "coordinates": {"latitude": -4.0435, "longitude": 39.6682},
            "climate": {
                "peak_sun_hours": 5.8,
                "avg_temperature": 26.7,
                "rainfall_mm_per_year": 1050,
                "humidity_percent": 80
            },
            "elevation": 50,  # meters above sea level
            "region": "Coast"
        },
        "Kwale": {
            "coordinates": {"latitude": -4.1821, "longitude": 39.4662},
            "climate": {
                "peak_sun_hours": 5.7,
                "avg_temperature": 26.5,
                "rainfall_mm_per_year": 1200,
                "humidity_percent": 78
            },
            "elevation": 305,
            "region": "Coast"
        },
        "Kilifi": {
            "coordinates": {"latitude": -3.6302, "longitude": 39.8499},
            "climate": {
                "peak_sun_hours": 5.7,
                "avg_temperature": 27.0,
                "rainfall_mm_per_year": 1000,
                "humidity_percent": 76
            },
            "elevation": 156,
            "region": "Coast"
        },
        "Tana River": {
            "coordinates": {"latitude": -1.5002, "longitude": 39.7839},
            "climate": {
                "peak_sun_hours": 5.8,
                "avg_temperature": 28.5,
                "rainfall_mm_per_year": 450,
                "humidity_percent": 65
            },
            "elevation": 232,
            "region": "Coast"
        },
        "Lamu": {
            "coordinates": {"latitude": -2.2717, "longitude": 40.9022},
            "climate": {
                "peak_sun_hours": 5.9,
                "avg_temperature": 27.8,
                "rainfall_mm_per_year": 950,
                "humidity_percent": 79
            },
            "elevation": 10,
            "region": "Coast"
        },
        "Taita-Taveta": {
            "coordinates": {"latitude": -3.3999, "longitude": 38.5651},
            "climate": {
                "peak_sun_hours": 5.8,
                "avg_temperature": 24.5,
                "rainfall_mm_per_year": 650,
                "humidity_percent": 70
            },
            "elevation": 830,
            "region": "Coast"
        },
        "Garissa": {
            "coordinates": {"latitude": -0.4550, "longitude": 39.6406},
            "climate": {
                "peak_sun_hours": 6.0,
                "avg_temperature": 29.5,
                "rainfall_mm_per_year": 350,
                "humidity_percent": 56
            },
            "elevation": 151,
            "region": "North Eastern"
        },
        "Wajir": {
            "coordinates": {"latitude": 1.7471, "longitude": 40.0573},
            "climate": {
                "peak_sun_hours": 6.2,
                "avg_temperature": 29.8,
                "rainfall_mm_per_year": 250,
                "humidity_percent": 52
            },
            "elevation": 244,
            "region": "North Eastern"
        },
        "Mandera": {
            "coordinates": {"latitude": 3.9360, "longitude": 41.8675},
            "climate": {
                "peak_sun_hours": 6.3,
                "avg_temperature": 30.2,
                "rainfall_mm_per_year": 250,
                "humidity_percent": 50
            },
            "elevation": 418,
            "region": "North Eastern"
        },
        "Marsabit": {
            "coordinates": {"latitude": 2.3359, "longitude": 37.9946},
            "climate": {
                "peak_sun_hours": 6.1,
                "avg_temperature": 22.5,
                "rainfall_mm_per_year": 250,
                "humidity_percent": 56
            },
            "elevation": 1345,
            "region": "Eastern"
        },
        "Isiolo": {
            "coordinates": {"latitude": 0.3535, "longitude": 37.5822},
            "climate": {
                "peak_sun_hours": 5.9,
                "avg_temperature": 26.0,
                "rainfall_mm_per_year": 350,
                "humidity_percent": 58
            },
            "elevation": 1145,
            "region": "Eastern"
        },
        "Meru": {
            "coordinates": {"latitude": 0.0478, "longitude": 37.6431},
            "climate": {
                "peak_sun_hours": 5.7,
                "avg_temperature": 21.5,
                "rainfall_mm_per_year": 1250,
                "humidity_percent": 70
            },
            "elevation": 1564,
            "region": "Eastern"
        },
        "Tharaka-Nithi": {
            "coordinates": {"latitude": -0.3073, "longitude": 37.6431},
            "climate": {
                "peak_sun_hours": 5.6,
                "avg_temperature": 22.0,
                "rainfall_mm_per_year": 1150,
                "humidity_percent": 69
            },
            "elevation": 1380,
            "region": "Eastern"
        },
        "Embu": {
            "coordinates": {"latitude": -0.5390, "longitude": 37.4597},
            "climate": {
                "peak_sun_hours": 5.6,
                "avg_temperature": 21.8,
                "rainfall_mm_per_year": 1100,
                "humidity_percent": 72
            },
            "elevation": 1350,
            "region": "Eastern"
        },
        "Kitui": {
            "coordinates": {"latitude": -1.3671, "longitude": 38.0106},
            "climate": {
                "peak_sun_hours": 5.7,
                "avg_temperature": 25.0,
                "rainfall_mm_per_year": 750,
                "humidity_percent": 65
            },
            "elevation": 1130,
            "region": "Eastern"
        },
        "Machakos": {
            "coordinates": {"latitude": -1.5176, "longitude": 37.2636},
            "climate": {
                "peak_sun_hours": 5.8,
                "avg_temperature": 22.5,
                "rainfall_mm_per_year": 800,
                "humidity_percent": 65
            },
            "elevation": 1600,
            "region": "Eastern"
        },
        "Makueni": {
            "coordinates": {"latitude": -2.2569, "longitude": 37.8912},
            "climate": {
                "peak_sun_hours": 5.9,
                "avg_temperature": 23.5,
                "rainfall_mm_per_year": 600,
                "humidity_percent": 60
            },
            "elevation": 1000,
            "region": "Eastern"
        },
        "Nyandarua": {
            "coordinates": {"latitude": -0.1827, "longitude": 36.5228},
            "climate": {
                "peak_sun_hours": 5.4,
                "avg_temperature": 15.8,
                "rainfall_mm_per_year": 1200,
                "humidity_percent": 75
            },
            "elevation": 2500,
            "region": "Central"
        },
        "Nyeri": {
            "coordinates": {"latitude": -0.4169, "longitude": 36.9511},
            "climate": {
                "peak_sun_hours": 5.5,
                "avg_temperature": 17.5,
                "rainfall_mm_per_year": 1150,
                "humidity_percent": 74
            },
            "elevation": 1795,
            "region": "Central"
        },
        "Kirinyaga": {
            "coordinates": {"latitude": -0.6306, "longitude": 37.3124},
            "climate": {
                "peak_sun_hours": 5.6,
                "avg_temperature": 19.5,
                "rainfall_mm_per_year": 1300,
                "humidity_percent": 73
            },
            "elevation": 1230,
            "region": "Central"
        },
        "Murang'a": {
            "coordinates": {"latitude": -0.7948, "longitude": 37.1532},
            "climate": {
                "peak_sun_hours": 5.6,
                "avg_temperature": 19.8,
                "rainfall_mm_per_year": 1200,
                "humidity_percent": 72
            },
            "elevation": 1300,
            "region": "Central"
        },
        "Kiambu": {
            "coordinates": {"latitude": -1.0322, "longitude": 36.8359},
            "climate": {
                "peak_sun_hours": 5.6,
                "avg_temperature": 18.2,
                "rainfall_mm_per_year": 1100,
                "humidity_percent": 75
            },
            "elevation": 1720,
            "region": "Central"
        },
        "Turkana": {
            "coordinates": {"latitude": 3.1226, "longitude": 35.5947},
            "climate": {
                "peak_sun_hours": 6.2,
                "avg_temperature": 29.0,
                "rainfall_mm_per_year": 200,
                "humidity_percent": 40
            },
            "elevation": 600,
            "region": "Rift Valley"
        },
        "West Pokot": {
            "coordinates": {"latitude": 1.7688, "longitude": 35.1189},
            "climate": {
                "peak_sun_hours": 5.8,
                "avg_temperature": 23.5,
                "rainfall_mm_per_year": 800,
                "humidity_percent": 60
            },
            "elevation": 1800,
            "region": "Rift Valley"
        },
        "Samburu": {
            "coordinates": {"latitude": 1.0938, "longitude": 36.7229},
            "climate": {
                "peak_sun_hours": 5.9,
                "avg_temperature": 24.0,
                "rainfall_mm_per_year": 400,
                "humidity_percent": 58
            },
            "elevation": 1700,
            "region": "Rift Valley"
        },
        "Trans-Nzoia": {
            "coordinates": {"latitude": 1.0568, "longitude": 34.9500},
            "climate": {
                "peak_sun_hours": 5.5,
                "avg_temperature": 19.5,
                "rainfall_mm_per_year": 1200,
                "humidity_percent": 73
            },
            "elevation": 1800,
            "region": "Rift Valley"
        },
        "Uasin Gishu": {
            "coordinates": {"latitude": 0.5227, "longitude": 35.2696},
            "climate": {
                "peak_sun_hours": 5.6,
                "avg_temperature": 18.2,
                "rainfall_mm_per_year": 1100,
                "humidity_percent": 72
            },
            "elevation": 2100,
            "region": "Rift Valley"
        },
        "Elgeyo-Marakwet": {
            "coordinates": {"latitude": 0.8030, "longitude": 35.5087},
            "climate": {
                "peak_sun_hours": 5.7,
                "avg_temperature": 19.0,
                "rainfall_mm_per_year": 1200,
                "humidity_percent": 70
            },
            "elevation": 2400,
            "region": "Rift Valley"
        },
        "Nandi": {
            "coordinates": {"latitude": 0.1864, "longitude": 35.1171},
            "climate": {
                "peak_sun_hours": 5.6,
                "avg_temperature": 19.5,
                "rainfall_mm_per_year": 1350,
                "humidity_percent": 74
            },
            "elevation": 1850,
            "region": "Rift Valley"
        },
        "Baringo": {
            "coordinates": {"latitude": 0.4919, "longitude": 35.7420},
            "climate": {
                "peak_sun_hours": 5.8,
                "avg_temperature": 21.0,
                "rainfall_mm_per_year": 800,
                "humidity_percent": 65
            },
            "elevation": 1200,
            "region": "Rift Valley"
        },
        "Laikipia": {
            "coordinates": {"latitude": 0.3998, "longitude": 36.7820},
            "climate": {
                "peak_sun_hours": 5.7,
                "avg_temperature": 18.5,
                "rainfall_mm_per_year": 750,
                "humidity_percent": 68
            },
            "elevation": 1700,
            "region": "Rift Valley"
        },
        "Nakuru": {
            "coordinates": {"latitude": -0.3031, "longitude": 36.0800},
            "climate": {
                "peak_sun_hours": 5.6,
                "avg_temperature": 18.0,
                "rainfall_mm_per_year": 950,
                "humidity_percent": 70
            },
            "elevation": 1850,
            "region": "Rift Valley"
        },
        "Narok": {
            "coordinates": {"latitude": -1.0876, "longitude": 35.8704},
            "climate": {
                "peak_sun_hours": 5.7,
                "avg_temperature": 19.5,
                "rainfall_mm_per_year": 950,
                "humidity_percent": 68
            },
            "elevation": 1890,
            "region": "Rift Valley"
        },
        "Kajiado": {
            "coordinates": {"latitude": -1.8518, "longitude": 36.7820},
            "climate": {
                "peak_sun_hours": 5.8,
                "avg_temperature": 20.5,
                "rainfall_mm_per_year": 650,
                "humidity_percent": 60
            },
            "elevation": 1600,
            "region": "Rift Valley"
        },
        "Kericho": {
            "coordinates": {"latitude": -0.3643, "longitude": 35.2838},
            "climate": {
                "peak_sun_hours": 5.5,
                "avg_temperature": 17.5,
                "rainfall_mm_per_year": 1400,
                "humidity_percent": 75
            },
            "elevation": 2100,
            "region": "Rift Valley"
        },
        "Bomet": {
            "coordinates": {"latitude": -0.7868, "longitude": 35.3416},
            "climate": {
                "peak_sun_hours": 5.5,
                "avg_temperature": 18.0,
                "rainfall_mm_per_year": 1350,
                "humidity_percent": 74
            },
            "elevation": 1900,
            "region": "Rift Valley"
        },
        "Kakamega": {
            "coordinates": {"latitude": 0.2827, "longitude": 34.7519},
            "climate": {
                "peak_sun_hours": 5.4,
                "avg_temperature": 21.0,
                "rainfall_mm_per_year": 1900,
                "humidity_percent": 76
            },
            "elevation": 1520,
            "region": "Western"
        },
        "Vihiga": {
            "coordinates": {"latitude": 0.0837, "longitude": 34.7223},
            "climate": {
                "peak_sun_hours": 5.4,
                "avg_temperature": 20.8,
                "rainfall_mm_per_year": 1900,
                "humidity_percent": 77
            },
            "elevation": 1750,
            "region": "Western"
        },
        "Bungoma": {
            "coordinates": {"latitude": 0.5635, "longitude": 34.5595},
            "climate": {
                "peak_sun_hours": 5.4,
                "avg_temperature": 21.2,
                "rainfall_mm_per_year": 1650,
                "humidity_percent": 75
            },
            "elevation": 1400,
            "region": "Western"
        },
        "Busia": {
            "coordinates": {"latitude": 0.4582, "longitude": 34.1154},
            "climate": {
                "peak_sun_hours": 5.5,
                "avg_temperature": 22.5,
                "rainfall_mm_per_year": 1500,
                "humidity_percent": 75
            },
            "elevation": 1200,
            "region": "Western"
        },
        "Siaya": {
            "coordinates": {"latitude": 0.0623, "longitude": 34.2879},
            "climate": {
                "peak_sun_hours": 5.5,
                "avg_temperature": 22.8,
                "rainfall_mm_per_year": 1350,
                "humidity_percent": 73
            },
            "elevation": 1200,
            "region": "Nyanza"
        },
        "Kisumu": {
            "coordinates": {"latitude": -0.1022, "longitude": 34.7617},
            "climate": {
                "peak_sun_hours": 5.5,
                "avg_temperature": 23.0,
                "rainfall_mm_per_year": 1400,
                "humidity_percent": 73
            },
            "elevation": 1150,
            "region": "Nyanza"
        },
        "Homa Bay": {
            "coordinates": {"latitude": -0.5270, "longitude": 34.4571},
            "climate": {
                "peak_sun_hours": 5.6,
                "avg_temperature": 22.5,
                "rainfall_mm_per_year": 1200,
                "humidity_percent": 70
            },
            "elevation": 1200,
            "region": "Nyanza"
        },
        "Migori": {
            "coordinates": {"latitude": -1.0634, "longitude": 34.4731},
            "climate": {
                "peak_sun_hours": 5.6,
                "avg_temperature": 22.0,
                "rainfall_mm_per_year": 1300,
                "humidity_percent": 69
            },
            "elevation": 1400,
            "region": "Nyanza"
        },
        "Kisii": {
            "coordinates": {"latitude": -0.6698, "longitude": 34.7893},
            "climate": {
                "peak_sun_hours": 5.5,
                "avg_temperature": 19.8,
                "rainfall_mm_per_year": 1800,
                "humidity_percent": 75
            },
            "elevation": 1700,
            "region": "Nyanza"
        },
        "Nyamira": {
            "coordinates": {"latitude": -0.5570, "longitude": 35.0019},
            "climate": {
                "peak_sun_hours": 5.5,
                "avg_temperature": 19.0,
                "rainfall_mm_per_year": 1800,
                "humidity_percent": 75
            },
            "elevation": 1800,
            "region": "Nyanza"
        },
        "Nairobi": {
            "coordinates": {"latitude": -1.2921, "longitude": 36.8219},
            "climate": {
                "peak_sun_hours": 5.7,
                "avg_temperature": 19.0,
                "rainfall_mm_per_year": 1050,
                "humidity_percent": 71
            },
            "elevation": 1795,
            "region": "Nairobi"
        }
    }
    
    return counties

def get_county_regions():
    """Return a list of Kenya's administrative regions"""
    return {
        "Coast": ["Mombasa", "Kwale", "Kilifi", "Tana River", "Lamu", "Taita-Taveta"],
        "North Eastern": ["Garissa", "Wajir", "Mandera"],
        "Eastern": ["Marsabit", "Isiolo", "Meru", "Tharaka-Nithi", "Embu", "Kitui", "Machakos", "Makueni"],
        "Central": ["Nyandarua", "Nyeri", "Kirinyaga", "Murang'a", "Kiambu"],
        "Rift Valley": ["Turkana", "West Pokot", "Samburu", "Trans-Nzoia", "Uasin Gishu", "Elgeyo-Marakwet", 
                       "Nandi", "Baringo", "Laikipia", "Nakuru", "Narok", "Kajiado", "Kericho", "Bomet"],
        "Western": ["Kakamega", "Vihiga", "Bungoma", "Busia"],
        "Nyanza": ["Siaya", "Kisumu", "Homa Bay", "Migori", "Kisii", "Nyamira"],
        "Nairobi": ["Nairobi"]
    }