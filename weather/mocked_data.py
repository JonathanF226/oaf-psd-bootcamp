from abstract_ds import Service
import numpy as np

class MockedDataService(Service):
    """Mocked data class that simulates getting temperature data."""

    def get_data(self) -> dict:
        """This method will generate 5 random temperatures for the set times and return it as a dictionary."""
        temperatures = np.random.uniform(low=60, high=80, size=5)  
        
        times = ["12 PM", "1 PM", "2 PM", "3 PM", "4 PM"] 
        
        return {
            "hourly": {
                "time": times,
                "temperature": temperatures.tolist()
            }
        }