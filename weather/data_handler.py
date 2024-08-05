from abstract_ds import Service
from api_data import APICallingService
from mocked_data import MockedDataService
class DataServiceHandler:
    """Data Service Handler class handles data retrieval and output based on the provided service."""

    def __init__(self, service: Service):
        """Initializes the DataServiceHandler with a specific service."""
        self.service = service

    def print_data(self) -> None:
        """This method retrieves and prints or plots data based on the type of service."""
        data = self.service.get_data()

        if isinstance(self.service, APICallingService):
            self.service.plot_data(data)  
        elif isinstance(self.service, MockedDataService):
            print(data)  
        else:
            print("Unsupported service type.")
