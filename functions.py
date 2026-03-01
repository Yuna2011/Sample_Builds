import requests # Must import requests so we can use API
 

# API Base URL for PokéAPI
API_URL = "https://dog.ceo/api/breeds/list/all"

# Dictionary to store collected Pokémon
dog_list = {}

def search_dog(name):
    """Search for an animal by name or ID and return its details.""" # Triple quotes is a docstring - allows multiline comments!
    response = requests.get(f"{API_URL}{name.lower()}")
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"].capitalize(),
            "class": data["class"],
            "height": data["height"],
            "weight": data["weight"],
        }
    else:
        print("dog breed not found.")
        return None
    
def add_dog(name):
    """Add a dog breed to the list."""
    dog = search_dog(name)
    if dog:
        dog_list[dog["name"]] = dog
        print(f"{dog['name']} added to list.")

def view_dog_list():
    """Display all collected Pokémon."""
    if dog_list:
        for name, details in dog_list.items():
            print(f"{name} - ID: {details['id']}, Height: {details['height']}, Weight: {details['weight']}")
    else:
        print("Your dog breed list is empty.")

def remove_dog(name):
    """Remove a Pokémon from the Pokédex."""
    if name.capitalize() in dog_list:
        del dog_list[name.capitalize()]
        print(f"{name.capitalize()} removed from list.")
    else:
        print("Dog breed not found in your list.")


#pip install -r requirements.txt

