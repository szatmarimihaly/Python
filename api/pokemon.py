import requests
# json <Response [200]> -> should be okay

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    #print(response)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f'Failed to retrieve data {response.status_code}' )

pokemon_name = "ditto" 
pokemon_info = get_pokemon(pokemon_name)

if pokemon_info:
    print(f'Name: {pokemon_info['name']}')
    print(f'Id: {pokemon_info['id']}')
    print(f'Height: {pokemon_info['height']}')
    print(f'Weight: {pokemon_info['weight']}')


