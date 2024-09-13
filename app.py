import csv
import time
from prometheus_client import start_http_server, Gauge

# Gauges for temperature and humidity metrics
temperature_gauge = Gauge('city_temperature', 'Temperature of the city in Celsius', ['city'])
humidity_gauge = Gauge('city_humidity', 'Humidity level in the city in percentage', ['city'])

# Function to read weather data from CSV
def read_weather_data(weather_data):
    with open(weather_data, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            yield row

# Function to push metrics to Prometheus
def push_metrics():
    for weather_data in read_weather_data('weather_data.csv'):
        city = weather_data['City']
        temperature = float(weather_data['Temperature'])
        humidity = float(weather_data['Humidity'])

        # Update the Prometheus metrics
        temperature_gauge.labels(city=city).set(temperature)
        humidity_gauge.labels(city=city).set(humidity)

        print(f"City: {city}, Temp: {temperature}°C, Humidity: {humidity}%")

        # Sleep for 2 seconds between updates
        time.sleep(2)

if __name__ == "__main__":
    # Start Prometheus metrics server on port 8000 to expose metrics
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000")
    
    # Push the weather metrics continuously
    push_metrics()
