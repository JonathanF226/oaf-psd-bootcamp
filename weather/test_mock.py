import unittest
from mocked_data import MockedDataService

class TestMockedDataService(unittest.TestCase):

    def setUp(self):
        """Set up the test case with a MockedDataService instance."""
        self.service = MockedDataService()

    def test_get_data_structure(self):
        """Test that the data returned by get_data has the correct structure."""
        data = self.service.get_data()
        self.assertIn("hourly", data)
        self.assertIn("time", data["hourly"])
        self.assertIn("temperature", data["hourly"])

    def test_get_data_content(self):
        """Test that the data returned by get_data contains the correct number of entries."""
        data = self.service.get_data()
        self.assertEqual(len(data["hourly"]["time"]), 5)
        self.assertEqual(len(data["hourly"]["temperature"]), 5)

if __name__ == "__main__":
    unittest.main()
