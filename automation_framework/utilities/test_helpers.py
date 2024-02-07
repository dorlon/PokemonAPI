# get all type JSON data from API
def get_pokemon_types(api):
    response = api.get_types()
    data = response.json()
    return data


# get specific JSON type data
def get_pokemon_type_data(api, type):
    response = api.get_pokemons_by_type(type)
    data = response.json()
    return data


# get the data of pokemon chosen from 'pokemonURL'
def get_pokemon_data(api, pokemonURL):
    response = api.get_pokemon_data(pokemonURL)
    data = response.json()
    return data
