import requests
base_url = "https://pokeapi.co/api/v2/"

def get_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    data = response.json()
    
    if (response.status_code != 200):
        return None
    return {"name":data["name"].capitalize(),
            "id":data["id"],
            "weight":data["weight"],
            "height":data["height"]
            }
info = get_info("pikachu")
print (info)