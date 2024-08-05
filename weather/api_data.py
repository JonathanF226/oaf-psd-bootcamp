from abstract_ds import Service
import requests
import matplotlib.pyplot as plt


class APICallingService(Service):
    """API data class for fetching and plotting temperature data."""

    def get_data(self) -> dict:
        """This method gets data from API for New York and returns it as a dictionary."""
        response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=40.7143&longitude=-74.006&current=temperature_2m&hourly=temperature_2m&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch')
        return response.json()
    
    def plot_data(self, data: dict) -> None:
        """This method plots the hourly temperature from the API."""
        hourly_temps = data.get('hourly', {}).get('temperature_2m', [])
        hourly_times = data.get('hourly', {}).get('time', [])
        
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