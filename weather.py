class WeatherFetcher:
    """This class is in charge of getting data from API.

    The API should probably be in a .env file for security reasons. If not we can pass the API key directly here.
    """
    def __init__(self) -> None:
        """Can pass the API key here and URL"""
        pass

    def fetch_weather_data(self, city: str) -> dict:
        """This method will get the data from an API for a given city and return in a dictionary"""
        pass

class WeatherData:
    """This class will get specific data from the dictionary and return it."""

    def __init__(self, weather_data: dict) -> None:
        """Initialize with fetched data"""
        pass

    def get_temperature(self) -> float:
        """This method will get and return temperature from the dictionary"""
        pass

    def get_humidity(self) -> float:
        """This method will get and return humidity from the dictionary"""
        pass

class WeatherDisplay:
    """This class will be in charge of displaying data."""

    def __init__(self, temperature: float, humidity: float) -> None:
        """Initialize with temperature and humidity"""
        pass

    def display_weather(self) -> None:
        """Display weather data such as temperature and humidity"""
        pass

    