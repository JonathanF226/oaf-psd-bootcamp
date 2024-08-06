import unittest
from data_handler import DataServiceHandler
from mocked_data import MockedDataService
from api_data import APICallingService

class TestDataServiceHandler(unittest.TestCase):

    def setUp(self):
        """Set up parameters for testing."""
        self.latitude = 40.7143
        self.longitude = -74.006

    def test_print_data_with_mocked_service(self):
        """Test DataServiceHandler with MockedDataService."""
        service = MockedDataService()
        handler = DataServiceHandler(service)
        
        data = service.get_data()
        self.assertIn("hourly", data)
        self.assertIn("time", data["hourly"])
        self.assertIn("temperature", data["hourly"])
        self.assertEqual(len(data["hourly"]["time"]), 5)
        self.assertEqual(len(data["hourly"]["temperature"]), 5)

    def test_print_data_with_api_service(self):
        """Test DataServiceHandler with APICallingService."""
        service = APICallingService()
        handler = DataServiceHandler(service)

        try:
            handler.print_data(self.latitude, self.longitude)
        except Exception as e:
            self.fail(f'plot_data raised an exception: {e}')

if __name__ == "__main__":
    unittest.main()