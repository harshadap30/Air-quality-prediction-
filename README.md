# Air Quality Monitoring and Prediction\

This Python script utilizes the OpenAQ API to fetch historical air quality data for a specific city and parameter (e.g., particulate matter PM2.5). It also fetches real-time data for prediction and generates a plot with historical data and a predicted future value.

## Description

The script consists of three main functions:

- fetch_historical_data(city, parameter, days):
- Fetches historical air quality data for a given city, parameter, and number of days.
- Uses the OpenAQ API to retrieve data within the specified date range.
- fetch_realtime_data(city, parameter):
- Fetches the latest real-time air quality data for a given city and parameter.
- Provides the current measurement value for prediction.
- plot_and_save_data(history, future_prediction, save_path='air_quality_plot.png'):
- Plots historical data and a predicted future value.
- Saves the plot as an image file (default: air_quality_plot.png).
- The main() function combines these functions to fetch historical data, obtain a real-time prediction, and generate a plot with both.

## How to Run
- Install required libraries:

## bash
- pip install requests matplotlib
- python script_name.py
  
Replace script_name.py with the actual name of your Python script.

### Note
The script uses the OpenAQ API, and the city parameter should be one of the cities mentioned in the API.
The parameter variable can be modified based on the specific air quality parameter of interest (e.g., 'pm10', 'co', 'so2').
Ensure an internet connection to fetch data from the OpenAQ API.
Feel free to explore and visualize air quality trends for different cities!
