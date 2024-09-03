import unittest
from api_data import APICallingService

class TestAPICallingService(unittest.TestCase):

    def setUp(self):
        self.service = APICallingService()
        self.latitude = 40.7143
        self.longitude = -74.006

    def test_get_data(self):
        """Test fetching data from the API."""
        data = self.service.get_data(self.latitude, self.longitude)
        self.assertIn('hourly', data)
        self.assertIn('time', data['hourly'])
        self.assertIn('temperature_2m', data['hourly'])

    def test_plot_data(self):
        """Test plotting the data fetched from the API."""
        data = self.service.get_data(self.latitude, self.longitude)
        hourly_times, hourly_temps = self.service.extract_temperature_data(data)
        try:
            self.service.plot_data(hourly_times, hourly_temps)
        except Exception as e:
            self.fail(f'plot_data raised an exception: {e}')

if __name__ == "__main__":
    unittest.main()