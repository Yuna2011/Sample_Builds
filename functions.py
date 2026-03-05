import requests # Must import requests so we can use API
 

# API Base URL for PokéAPI
API_URL = "https://hp-api.onrender.com/api/characters"

# Dictionary to store collected Pokémon
HP_list = {}

def search_character(name):
    """Search for character by name and return its details.""" # Triple quotes is a docstring - allows multiline comments!
    response = requests.get(f"{API_URL}{name.lower()}")
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"].capitalize(),
            "alternate_names": data["alternate_names"],
            "gender": data["gender"],
            "house": data["house"],
            "wand" : data["wand"]
        }
    else:
        print("Character not found.")
        return None
    
def add_character(name):
    """Add a character to the list."""
    hp = search_character(name)
    if hp:
        HP_list[hp["name"]] = hp
        print(f"{hp['name']} added to list.")

def view_character_list():
    """Display all collected characters."""
    if HP_list:
        for name, details in HP_list.items():
            print(f"{name} - ID: {details['id']}, Height: {details['height']}, Weight: {details['weight']}")
    else:
        print("Your list is empty.")

def remove_character(name):
    """Remove a Pokémon from the Pokédex."""
    if name.capitalize() in HP_list:
        del HP_list[name.capitalize()]
        print(f"{name.capitalize()} removed from list.")
    else:
        print("Character not found in your list.")


#pip install -r requirements.txt

