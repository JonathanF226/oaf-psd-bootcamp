"""This class is in charge of getting data from API.

The API should probably be in a .env file for security reasons. If not we can pass the API key directly here.
"""
class WeatherFetcher:
    """Can pass the API key here and URL"""
    def __init__(self) -> None:
        pass

    """This method will get the data from an API for a given city and return in a dictionary"""
    def fetch_weather_data(self, city: str) -> dict:
        pass

"""This class will get specific data from the dictionary and return it."""
class WeatherData:
    """Initialize with fetched data"""
    def __init__(self, weather_data: dict) -> None:
        pass

    """This method will get and return temperature from the dictionary"""
    def get_temperature(self) -> float:
        pass

    """This method will get and return humidity from the dictionary"""
    def get_humidity(self) -> float:
        pass

"""This class will be in charge of displaying data."""
class WeatherDisplay:
    """Initialize with temperature and humidity"""
    def __init__(self, temperature: float, humidity: float) -> None:
        pass

    """Display weather data such as temperature and humidity"""
    def display_weather(self) -> None:
        pass

