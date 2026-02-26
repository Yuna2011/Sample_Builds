import requests # Must import requests so we can use API
 

# API Base URL for PokéAPI
API_URL = "https://dog.ceo/dog-api/documentation/"

def search_animal(name):
    """Search for an animal by name or ID and return its details.""" # Triple quotes is a docstring - allows multiline comments!
    response = requests.get(f"{API_URL}{name.lower()}")
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"].capitalize(),
            "class": data["class"],
            "height": data["height"],
            "weight": data["weight"],
#            "types": [t["type"]["name"] for t in data["types"]]
        }
    else:
        print("animal not found.")
        return None


#pip install -r requirements.txt

