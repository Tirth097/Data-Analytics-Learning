import requests
base_url = "https://pokeapi.co/api/v2"

def get_poki_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    data = response.json()
    
    return {
        "name":data["name"].capitalize(),
        "id: ":data["id"],
        "weight":data["weight"],
        "height":data["height"]
    }
info = get_poki_info("pikachu")
print(info)   

    
    