from abstract_ds import Service
from api_data import APICallingService
from mocked_data import MockedDataService
class DataServiceHandler:
    """Data Service Handler class handles data retrieval and output based on the provided service."""

    def __init__(self, service: Service):
        """Initializes the DataServiceHandler with a specific service."""
        self.service = service

    def print_data(self, latitude: float, longitude: float) -> None:
        """This method retrieves and prints or plots data based on the type of service."""
        if isinstance(self.service, APICallingService):
            data = self.service.get_data(latitude, longitude)
            hourly_times, hourly_temps = self.service.extract_temperature_data(data)
            self.service.plot_data(hourly_times, hourly_temps) 
        elif isinstance(self.service, MockedDataService):
            data = self.service.get_data()
            print(data)  
        else:
            print("Unsupported service type.")
