import pytest
from automation_framework.utilities.api_helpers import ApiHelper
from automation_framework.utilities.test_helpers import get_pokemon_types
from automation_framework.utilities.test_helpers import get_pokemon_type_data
from automation_framework.utilities.test_helpers import get_pokemon_data




# Using API functions from: api_helpers.py
@pytest.fixture(scope="module")
def api():
    return ApiHelper()


# Verify value count of types are: 20
# Also, checks the types are different
def test_get_count_types(api):
    data = get_pokemon_types(api)
    uniques = {result['name'] for result in data['results']}
    assert len(uniques) == 20, "There should be 20 unique type names"


# Validate id of fire type
# Validate the pokemon chosen is exist in the list of chosen type
# Also, checking if pokemon is not exist in the list of chosen type
def test_validate_pokemon_type(api):
    data = get_pokemon_type_data(api, "fire")
    assert data["id"] == 10
    namesList = [result['pokemon']['name'] for result in data['pokemon']]
    assert 'charmander' in namesList
    assert 'bulbasaur' not in namesList


# Keep the weights and URLs from specific type. ("pokemon_url", "pokemon_weight")
# "heaviest_pokemon" is an array of objects who keeps the names and the weights of every pokemon
# And finally we present the 5 heaviest pokemons from "heaviest_pokemon"
def test_validate_five_heaviest_pokemons(api):
    heaviest_pokemon = []
    data = get_pokemon_type_data(api, "fire")
    for entry in data["pokemon"]:
        pokemon_url = entry["pokemon"]["url"]
        pokemon_weight = get_pokemon_data(api, pokemon_url)["weight"]

        heaviest_pokemon.append({"name": entry["pokemon"]["name"], "weight": pokemon_weight})
    heaviest_pokemon.sort(key=lambda x: x["weight"], reverse=True)
    for pokemon in heaviest_pokemon[:5]:
        print(f"{pokemon['name']}: Weight - {pokemon['weight']}")