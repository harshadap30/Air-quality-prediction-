import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def fetch_historical_data(city, parameter, days):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    url = f'https://api.openaq.org/v1/measurements?city={city}&parameter={parameter}&date_from={start_date.isoformat()}&date_to={end_date.isoformat()}'
    response = requests.get(url)
    data = response.json()
    print("API Response:", data)

    if 'results' in data:
        return [entry['value'] for entry in data['results']]
    else:
        print("Error fetching historical data")
        return []

def fetch_realtime_data(city, parameter):
    url = f'https://api.openaq.org/v1/latest?city={city}&parameter={parameter}'
    response = requests.get(url)
    data = response.json()

    if 'results' in data:
        return data['results'][0]['measurements'][0]['value']
    else:
        print("Error fetching real-time data")
        return None


def plot_and_save_data(history, future_prediction, save_path='air_quality_plot.png'):
    plt.plot(history, label='Historical Data')
    plt.axhline(y=future_prediction, color='r', linestyle='--', label='Predicted Future Value')
    plt.xlabel('Time')
    plt.ylabel('Air Quality Index')
    plt.title('Air Quality Monitoring and Prediction')
    plt.legend()
    plt.savefig(save_path)


    # plt.show()
    print(plt)
    

def main():
    city = 'Abu Dhabi'
    print(city)
    parameter = 'pm25'  # Modify based on the parameter you are interested in (e.g., 'pm10', 'co', 'so2', etc.)
    historical_days = 30

    # Fetch historical data
    historical_data = fetch_historical_data(city, parameter, historical_days)

    if not historical_data:
        return

    # Fetch real-time data for prediction
    current_prediction = fetch_realtime_data(city, parameter)
    print("Historical Data:", historical_data)
    print("Current Prediction:", current_prediction)
    

    if current_prediction is not None:
        # Combine historical data and predicted future value
        all_data = historical_data + [current_prediction]


                # Plot the data and save as an image
        plot_and_save_data(all_data, current_prediction)

if __name__ == "__main__":
    main()
