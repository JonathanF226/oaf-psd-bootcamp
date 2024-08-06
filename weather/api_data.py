from abstract_ds import Service
import requests
import matplotlib.pyplot as plt


class APICallingService(Service):
    """API data class for fetching and plotting temperature data."""

    def get_data(self, latitude: float, longitude: float, hourly: str = "temperature_2m", temperature_unit: str = "fahrenheit") -> dict:
        """This method gets data from API for New York and returns it as a dictionary."""
        base_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'hourly': hourly,
            'temperature_unit': temperature_unit,
        }
        response = requests.get(base_url, params=params)

        if response.status_code != 200:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")
            return {}
        try:
            data = response.json()
        except ValueError:
            print("Error: Unable to parse JSON response.")
            return {}

        if 'hourly' not in data or 'temperature_2m' not in data['hourly']:
            print("Error: Required data not found in the response.")
            return {}

        return data
    
    def extract_temperature_data(self, data: dict) -> tuple:
        """This method extracts hourly temperature and time data from the API response."""
        hourly_temps = data.get('hourly', {}).get('temperature_2m', [])
        hourly_times = data.get('hourly', {}).get('time', [])
        
        return hourly_times, hourly_temps
    
    def plot_data(self, hourly_times: list, hourly_temps: list) -> None:
        """This method plots the hourly temperature from the API."""
        if not hourly_temps or not hourly_times:
            print("No hourly temperature data available.")
            return
        
        plt.figure(figsize=(12, 6))
        plt.plot(hourly_times, hourly_temps, marker='o', linestyle='-', color='b')
        plt.xlabel('Time')
        plt.ylabel('Temperature (°F)')
        plt.title('Hourly Temperature Forecast')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()