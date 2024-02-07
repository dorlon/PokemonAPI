import requests
import configparser


# class of functions for API to get pokemons data
class ApiHelper:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('automation_framework/config/config.ini')
        self.BASE_URL = config.get('URL', 'BASE_URL')

    # get all existing types
    def get_types(self):
        url = f"{self.BASE_URL}/type"
        response = requests.get(url)
        return response

    # get the data of specific type chosen in 'kindOfType'
    def get_pokemons_by_type(self, kindOfType):
        url = f"{self.BASE_URL}/type/{kindOfType}"
        response = requests.get(url)
        return response

    def get_pokemon_data(self, pokemonURL):
        response = requests.get(pokemonURL)
        return response
