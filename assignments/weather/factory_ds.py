from mocked_data import MockedDataService
from api_data import APICallingService

class ServiceFactory:
    """Factory class for creating instances of different services."""

    def get_service(self, service_type: str):
        """This method returns an instance of a service based on the provided service type."""
        if service_type == "mocked":
            return MockedDataService()
        elif service_type == "api":
            return APICallingService()
        else:
            return None