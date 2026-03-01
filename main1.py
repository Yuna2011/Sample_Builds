from functions import *

def main():
    while True:
        print("Dog breed finder menu:")
        print("1. Search dog breed")
        print("2. Add dog breed to my list")
        print("3. View my list")
        print("4. Remove dog breed from my list")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter Animal name: ")
            search_dog(name)
            for key, value in search_dog(name).items(): 
              print(f"{key}: {value}")
        elif choice == "2":
            name = input("Enter dog breed name to add: ")
            add_dog(name)
        elif choice == "3":
            view_dog_list()
        elif choice == "4":
            name = input("Enter dog breed name to remove: ")
            remove_dog(name)
        elif choice == "5":
            print("Exiting list.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()