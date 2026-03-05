from functions import *

def main():
    while True:
        print("Harry Potter character finder menu:")
        print("1. Search character")
        print("2. Add charater to my list")
        print("3. View my list")
        print("4. Remove character from my list")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter character name: ")
            for key, value in search_character(name).items(): 
              print(f"{key}: {value}")
        elif choice == "2":
            name = input("Enter character to add: ")
            add_character(name)
        elif choice == "3":
            view_character_list()
        elif choice == "4":
            name = input("Enter character to remove: ")
            remove_character(name)
        elif choice == "5":
            print("Exiting list.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()