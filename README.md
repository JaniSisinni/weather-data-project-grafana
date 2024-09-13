Weather Monitoring with Prometheus and Grafana

This project demonstrates how to monitor weather data by reading from a CSV file and pushing metrics (e.g., temperature and humidity) to Prometheus. The metrics are then visualized using Grafana to provide real-time insights into weather conditions across different cities.

Table of Contents
1. Overview
2. Features
3. Project Structure
4. Installation
5. Running the Project
6. Prometheus Configuration
7. Grafana Dashboard Setup
8. Example Metrics
9. Dependencies
10. Contributing

1. Overview
This project reads weather data from a CSV file (simulated in fake_weather_data.csv), which contains columns for City, Temperature, and Humidity. It pushes these metrics to Prometheus using the Prometheus Python client. Prometheus scrapes the metrics at regular intervals, and Grafana provides an interactive dashboard to visualize the data.

The workflow is as follows:
- Python Script reads weather data and exposes it as metrics on an HTTP endpoint.
- Prometheus scrapes the metrics from the Python script and stores them.
- Grafana is used to visualize the metrics for monitoring purposes.

2. Features
Monitor real-time weather data (temperature and humidity) from various cities.
Push metrics to Prometheus using Python.
Visualize and analyze data in Grafana dashboards.
Easily extensible to include more metrics or different types of data.
CSV-based data input for ease of use.

3. Project Structure
weather-monitoring/
│
├── app.py                   # Python script that reads data from CSV and pushes metrics to Prometheus
├── fake_weather_data.csv     # CSV file containing weather data for various cities
├── prometheus.yml            # Prometheus configuration file
└── README.md                 # Project documentation

4. Installation
- Prerequisites
Python 3.6+
Prometheus
Grafana

4.1 Clone the Repository
git clone https://github.com/JaniSisinni/weather-monitoring.git
cd weather-monitoring

4.2 You need the prometheus_client library to expose the metrics:
pip install prometheus_client

4.3 Install Prometheus
    Download Prometheus from the official website.
    Place the provided prometheus.yml configuration file in the same directory as your Prometheus binary.
    Start prometheus: ./prometheus --config.file=prometheus.yml

4.4 Install Grafana
    Download Grafana from the official website.
    Start Grafana and access it at http://localhost:3000.
    Log in using the default credentials (username: admin, password: admin)

5. Running the project
5.1 Start the py script: python app.py
5.2 Verify Prometheus is Scraping Metrics:
Once the Python script is running, Prometheus should automatically scrape the metrics. You can verify this by visiting http://localhost:9090/targets in your browser and checking that the weather_app target is active.

You can also query the metrics in Prometheus by going to http://localhost:9090/graph and running queries like:
city_temperature
city_humidity

6. Prometheus Configuration
The content of the prometheus.yml ensures Prometheus scrapes the metrics exposed at localhost:8000

7. Grafana Dashboard Setup
7.1 Add Prometheus as a Data Source:
    In Grafana, go to Configuration > Data Sources and add Prometheus
    Set the URL to your Prometheus server (e.g., http://localhost:9090)
7.2 Create a Dashboard:
    Go to Create > Dashboard and add a new panel
    In the Query section, use one of the following PromQL queries:
        city_temperature
        city_humidity
7.3 Save the Dashboard and use it to monitor the weather data in real-time

8. Example Metrics
    city_temperature: Tracks the temperature (°C) for each city
    city_humidity: Tracks the humidity (%) for each city

9. Dependencies
The Python package prometheus_client is required: 
    pip install prometheus_client

10. Contributing
Contributions are welcome! If you'd like to contribute to the project, please fork the repository and create a pull request with your changes. Feel free to open issues for feature requests or bugs.
