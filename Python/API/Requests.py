import requests # in terminal "pip install requests"
base_url="https://pokeapi.co/api/v2/" 

def get_poki_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url) #using get method and storing it in response url
    #print(response) # gives status code (http) eg: 404 -> not found ; 200 -> response is ok
    if response.status_code == 200:
        pokemon_data = response.json()#converts data into dictonary
        return pokemon_data
       # print(f"Data found {response.status_code}")
    else:
        print(f"Data not found {response.status_code}")
    
pokemon_info = get_poki_info("greninja")
if pokemon_info:
    print(f"name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"weight: {pokemon_info["weight"]}")
    print(f"height: {pokemon_info["height"]}")
    
