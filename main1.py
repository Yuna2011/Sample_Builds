from functions import *

def main():
    while True:
        print("Animal Finder menu:")
        print("1. Search Animal")
#        print("2. Add Pokémon to Pokédex")
#        print("3. View Pokédex")
#        print("4. Remove Pokémon")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter Animal name: ")
            search_animal(name)
            for key, value in search_animal(name).items(): 
              print(f"{key}: {value}")
#        elif choice == "2":
#            name = input("Enter Pokémon name to add: ")
#            add_pokemon(name)
#        elif choice == "3":
#            view_pokedex()
#        elif choice == "4":
#            name = input("Enter Pokémon name to remove: ")
#            remove_pokemon(name)
#        elif choice == "5":
#            print("Exiting Pokédex.")
#            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()