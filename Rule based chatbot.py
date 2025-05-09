#name the file as main.py , uncomment the imports and basic functions, complete  the code by writing remainig functions 

import re, random
from colorama import Fore, init

# # Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# # Destination & joke data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# # Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Provide travel recommendations (recursive if user rejects suggestions)
def recommend():
    print(Fore.CYAN + "I can recommend some great travel destinations!")
    print("1. Beaches")
    print("2. Mountains")
    print("3. Cities")
    choice = input("Which type of destination do you prefer? (beaches/mountains/cities): ")
    
    choice = normalize_input(choice)
    
    if choice in destinations:
        print(Fore.GREEN + f"Great choice! Here are some {choice} destinations:")
        for place in destinations[choice]:
            print(f"- {place}")
    else:
        print(Fore.RED + "I'm sorry, I didn't understand that. Let's try again.")
        recommend()

# Offer packing tips based on user’s destination and duration
def packing_tips():
    print(Fore.CYAN + "I can help you with packing tips!")
    destination = input("Where are you going? (beaches/mountains/cities): ")
    duration = input("How many days will you be traveling? ")

    destination = normalize_input(destination)
    duration = normalize_input(duration)

    if destination in destinations:
        print(Fore.GREEN + f"Packing tips for {destination} for {duration} days:")
        if destination == "beaches":
            print("- Sunscreen")
            print("- Swimwear")
            print("- Sunglasses")
        elif destination == "mountains":
            print("- Warm clothing")
            print("- Hiking boots")
            print("- First-aid kit")
        elif destination == "cities":
            print("- Comfortable shoes")
            print("- City map or guide")
            print("- Portable charger")
    else:
        print(Fore.RED + "I'm sorry, can you plese specify any of the given options(beaches/mountains/cities)?")
# Tell a random joke
def telljoke():
    print(Fore.CYAN + "Oh i get it , so here's a joke for you :\n "+ random.choice(jokes))
# Display help menu
def help_menu():
    print(Fore.CYAN + "I can assist you with following things today:")
    print("1. Travel recommendations")
    print("2. Packing tips")
    print("3. Tell a joke")
    print("4. Help menu")
    print("5. Exit")

# Main chat loop
def chat():
    name = input("Please enter your name: ")
    print(Fore.CYAN + f"Hello {name}! welcome to the Equilibra (The name of the travel chatbot) , What can i help you with today?")
   
    help_menu()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)
        if user_input == "1":
            recommend()
        elif user_input == "thanks" or user_input == "thank you":
            print(Fore.MAGENTA + "You're welcome! If you need anything else, just ask.")
        elif user_input == "2":
            packing_tips()
        elif user_input == "3":
            telljoke()
        elif user_input == "4":
            help_menu()
        elif user_input == "5" or user_input == "exit":
            print(Fore.GREEN + "Goodbye! Have a great day!")
            break
        else:
            print(Fore.RED + "I'm sorry, I didn't understand that. Please try again.")


# Run the chatbot
if __name__ == "__main__":
    chat()
