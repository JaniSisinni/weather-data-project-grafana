import pandas as pd
import numpy as np

# Function to generate random weather data
def generate_weather_data(countries, start_year, end_year):
    data = {
        "Country": np.random.choice(countries, size=10000),
        "Year": np.random.randint(start_year, end_year + 1, size=10000),
        "Month": np.random.randint(1, 13, size=10000),
        "Day": np.random.randint(1, 31, size=10000),
        "Temperature (Celsius)": np.random.uniform(-10, 30, size=10000),
        "Precipitation (mm)": np.random.uniform(0, 100, size=10000),
        "Wind Speed (km/h)": np.random.uniform(5, 40, size=10000)
    }
    return pd.DataFrame(data)

# List of countries
countries = ["United Kingdom", "France", "Germany", "Spain", "Italy"]

# Generate data and save to CSV
df = generate_weather_data(countries, 2000, 2024)
df.to_csv("weather_data.csv", index=False)