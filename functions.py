import requests # Must import requests so we can use API

# API Base URL for PokéAPI
API_URL = "https://hp-api.onrender.com/api/characters"

# Dictionary to store collected Pokémon
HP_list = {}

def search_character(name):
    response = requests.get(API_URL)
    if response.status_code != 200:
        print("API error.")
        return None

    characters = response.json()

    # Find first matching character (case-insensitive)
    for c in characters:
        if c["name"].lower() == name.lower():
            return {
                "name": c["name"],
                "nickname": c["alternate_names"],
                "gender": c["gender"],
                "house": c["house"],
                "wand": c["wand"]
            }

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
            print(f"{name} - Gender: {details['gender']}, House: {details['house']}, Wand: {details['wand']}")
    else:
        print("Your list is empty.")

def remove_character(name):
    """Remove a Character from the list."""
    if name in HP_list:
        del HP_list[name]
        print(f"{name.capitalize()} removed from list.")
    else:
        print("Character not found in your list.")



