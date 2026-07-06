import re
import random
from colorama import Fore, init

# Initialize Colorama
init(autoreset=True)

# Study resources
subjects = {
    "python": ["Practice loops", "Learn functions", "Solve coding problems"],
    "java": ["Revise OOP concepts", "Practice inheritance", "Build a mini project"],
    "math": ["Practice algebra", "Solve geometry questions", "Revise formulas"]
}

facts = [
    "The first computer programmer was Ada Lovelace.",
    "Python was created by Guido van Rossum.",
    "Learning a little every day is more effective than studying for hours once a week."
]

# Clean user input
def clean_text(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Recommend study topics
def suggest_topic():
    print(Fore.CYAN + "StudyBot: Which subject are you studying? (Python, Java, Math)")
    subject = clean_text(input(Fore.YELLOW + "You: "))

    if subject in subjects:
        tip = random.choice(subjects[subject])
        print(Fore.GREEN + f"StudyBot: You can start with: {tip}")

        choice = clean_text(input(Fore.CYAN + "Would you like another suggestion? (yes/no): "))

        if choice == "yes":
            suggest_topic()
        else:
            print(Fore.GREEN + "StudyBot: Happy studying!")
    else:
        print(Fore.RED + "StudyBot: Sorry, I don't have suggestions for that subject.")

# Study tips
def study_tips():
    print(Fore.GREEN + "StudyBot: Here are some useful study tips:")
    print(Fore.GREEN + "- Take short breaks while studying.")
    print(Fore.GREEN + "- Practice regularly.")
    print(Fore.GREEN + "- Revise important topics every week.")

# Share a random fact
def fun_fact():
    print(Fore.MAGENTA + f"StudyBot: {random.choice(facts)}")

# Help menu
def help_menu():
    print(Fore.CYAN + "\nI can help you with:")
    print(Fore.GREEN + "- Study suggestions (type 'suggest')")
    print(Fore.GREEN + "- Study tips (type 'tips')")
    print(Fore.GREEN + "- Fun facts (type 'fact')")
    print(Fore.CYAN + "Type 'bye' to exit.\n")

# Main chatbot
def chatbot():
    print(Fore.CYAN + "Welcome! I'm StudyBot.")
    name = input(Fore.YELLOW + "What's your name? ")

    print(Fore.GREEN + f"Hello, {name}! Nice to meet you.")

    help_menu()

    while True:
        message = clean_text(input(Fore.YELLOW + f"{name}: "))

        if "suggest" in message:
            suggest_topic()
        elif "tips" in message:
            study_tips()
        elif "fact" in message:
            fun_fact()
        elif "help" in message:
            help_menu()
        elif "bye" in message or "exit" in message:
            print(Fore.CYAN + "StudyBot: Goodbye! Have a great day.")
            break
        else:
            print(Fore.RED + "StudyBot: I didn't understand that. Type 'help' to see what I can do.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()