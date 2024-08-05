import unittest
from api_data import APICallingService

class TestAPICallingService(unittest.TestCase):

    def setUp(self):
        self.service = APICallingService()

    def test_get_data(self):
        """Test fetching data from the API."""
        data = self.service.get_data()
        self.assertIn('hourly', data)
        self.assertIn('time', data['hourly'])
        self.assertIn('temperature_2m', data['hourly'])

    def test_plot_data(self):
        """Test plotting the data fetched from the API."""
        data = self.service.get_data()
        try:
            self.service.plot_data(data)
        except Exception as e:
            self.fail(f'plot_data raised an exception: {e}')

if __name__ == "__main__":
    unittest.main()