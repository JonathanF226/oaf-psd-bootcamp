from typing import Tuple
from simple_term_menu import TerminalMenu
from dotenv import load_dotenv
import os 
import requests
from abc import ABC, abstractmethod
import sqlite3

def initialize_database():
    """
    Initializes the database by creating the 'favorites' table if it dose not already exist.
    """
    conn = sqlite3.connect('weather_app.db')
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY,
                city_name TEXT NOT NULL,
                units TEXT NOT NULL
            )               
        ''')
        conn.commit()
    finally:
        conn.close()

initialize_database()

load_dotenv()

API_KEY = os.getenv('ACCESS_TOKEN')

class Preferences(ABC):
    @abstractmethod
    def get_units(self) -> str:
        pass
    
    @abstractmethod
    def get_label(self) -> str:
        pass

class MetricPreferences(Preferences):
    def get_units(self) -> str:
        return 'metric'
    
    def get_label(self) -> str:
        return 'Celsius'

class ImperialPreferences(Preferences):
    def get_units(self) -> str:
        return 'imperial'
    
    def get_label(self) -> str:
        return 'Fahrenheit'

class KelvinPreferences(Preferences):
    def get_units(self) -> str:
        return 'standard'  

    def get_label(self) -> str:
        return 'Kelvin'  

class PreferencesFactory:
    @staticmethod
    def create_preferences(preference_type: str) -> Preferences:
        if preference_type == "metric":
            return MetricPreferences()
        elif preference_type == "imperial":
            return ImperialPreferences()
        elif preference_type == "standard":
            return KelvinPreferences()
        else:
            raise ValueError("Unknown preference type")


def save_favorite_city(city_name: str, prefernces: Preferences):
    """
    This method adds a city to the favorites table in the database.

    Args:
        city_name (str): The name of the city to be added to the favorites.
        preferences (Preferences): User's temperature unit preferences.

    Returns:
        None
    """
    conn = sqlite3.connect('weather_app.db')
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO favorites (city_name, units) VALUES (?,?)', (city_name,prefernces.get_units()))
        conn.commit()
        print(f"{city_name} has been added to your favorites!")
    finally:
        conn.close()


def show_favorites(api_key: str):
    """
    This method displays the user's favorite cities and allows them to view weather data for a selected city.

    This method retrieves the list of favorite cities from the 'favorites' table in the database.
    If the user has favorite cities saved, it presents them in a terminal menu for selection.
    Upon selecting a city, the function fetches and displays the weather data for that city.

    Args:
        api_key (str): The API key used for accessing the weather service.

    Returns:
        None
    """
    conn = sqlite3.connect('weather_app.db')

    try:
        cursor = conn.cursor()
        cursor.execute('SELECT city_name, units FROM favorites')
        favorites = cursor.fetchall()
    
        if favorites:
            print("Your favorite cities:")
            favorite_options = [f"{city} ({units})" for city, units in favorites]
            favorite_menu = TerminalMenu(favorite_options, title="Select a favorite city to view weather")
            favorite_index = favorite_menu.show()
            
            selected_city, selected_units = favorites[favorite_index]
            
            preferences = PreferencesFactory.create_preferences(selected_units.lower())
            
            search_city(api_key, preferences, selected_city)
        else:
            print("You have no favorite cities yet.")
    finally:
        conn.close()


def get_weather_data(city_name: str, api_key: str, preferences: Preferences) -> Tuple[list[str], list[float]]:
    """
    This method retrieves weather data for a specified city from the OpenWeatherMap API.

    This method sends a request to the OpenWeatherMap API to fetch the weather forecast 
    for the next 24 hours for the given city. The temperature units are determined 
    by the user's preferences.

    Args:
        city_name (str): The name of the city for which to fetch the weather data.
        api_key (str): The API key used to authenticate the request with OpenWeatherMap.
        preferences (Preferences): The user's temperature unit preferences.

    Returns:
        Tuple[list[str], list[float]]: A tuple containing two lists:
            - A list of date-time strings for each forecasted time period.
            - A list of temperatures corresponding to each date-time, in the units specified by preferences.
    """
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': preferences.get_units(), 
        'cnt': '24'  
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        json_data = response.json()
        
        times = [entry['dt_txt'] for entry in json_data['list']]
        temperatures = [entry['main']['temp'] for entry in json_data['list']]
        
        return times, temperatures
    except Exception as e:
        print(f"Error: {e}")
        return [], []


def is_city_favorited(city_name: str, preferences: Preferences) -> bool:
    """
    This method checks if a city is already in the user's favorites list.

    Args:
        city_name (str): The name of the city to check.
        preferences (Preferences): The user's temperature unit preferences.

    Returns:
        bool: True if the city is in the favorites list with the specified units, False otherwise.
    """
    conn = sqlite3.connect('weather_app.db')

    try:
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM favorites WHERE city_name = ? AND units = ?', (city_name, preferences.get_units()))
        result = cursor.fetchone()
        return result is not None
    finally:
        conn.close()


def search_city(api_key: str, preferences: Preferences, city_name: str = None):
    """
    This method prompts the user to enter a city name, fetches weather data for that city,
    and offers the option to save the city as a favorite.

    This method handles user interaction to obtain a city name (if not provided) and
    retrieves the weather forecast for that city using the OpenWeatherMap API. Then
    displays the data, checks if the city is already favorited, and optionally
    allows the user to add the city to their favorites list.

    Args:
        api_key (str): The API key used to authenticate requests with OpenWeatherMap.
        preferences (Preferences): The user's temperature unit preferences (e.g., metric, imperial).
        city_name (str, optional): The name of the city to search for. If not provided, the user will be prompted to enter it.
    
    Returns:
        None
    """
    if not city_name:
        city_name = input("Enter the city name: ")
    times, temperatures = get_weather_data(city_name, api_key, preferences)

    if times and temperatures:
        print(f"Weather data for {city_name}:")
        for time, temp in zip(times, temperatures):
            print(f"At {time}, the temperature is {temp} degrees {preferences.get_label()}")

        if is_city_favorited(city_name, preferences):
            print(f"{city_name} is already in your favorites.")
        else:
            favorite_options = ["Yes", "No"]
            favorite_menu = TerminalMenu(favorite_options, title="Do you want to add this city to your favorites?")
            favorite_index = favorite_menu.show()

            if favorite_index == 0:
                save_favorite_city(city_name, preferences)
    else:
        print("Failed to get data!")


def main():
    options = ["Search", "Favorites"]
    terminal_menu = TerminalMenu(options, search_key="/", title="Weather App Menu")
    menu_entry_index = terminal_menu.show()

    selected_option = options[menu_entry_index]
    print(f"You have selected {selected_option}!")

    if selected_option == "Search":
        # Preferences selection using menu
        preference_options = ["Metric (Celsius)", "Imperial (Fahrenheit)", "Standard (Kelvin)"]
        preference_menu = TerminalMenu(preference_options, title="Select Temperature Units")
        preference_index = preference_menu.show()
        
        if preference_index == 0:
            preference_input = "metric"
        elif preference_index == 1:
            preference_input = "imperial"
        elif preference_index == 2:
            preference_input = "standard"
        else:
            print("Invalid option selected.")
            return
        
        preferences = PreferencesFactory.create_preferences(preference_input)

        search_city(API_KEY, preferences)
    else:
        show_favorites(API_KEY)


if __name__ == "__main__":
    main()