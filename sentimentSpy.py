import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize Colorama
colorama.init()

print(f"{Fore.CYAN}Welcome to the Mood Analyzer!{Style.RESET_ALL}")

name = input(f"{Fore.MAGENTA}Enter your name: {Style.RESET_ALL}").strip()

if name == "":
    name = "Guest"

print(f"\n{Fore.CYAN}Hi, {name}!{Style.RESET_ALL}")
print("Type any sentence and I'll identify its sentiment.")
print(f"Commands: {Fore.YELLOW}history{Fore.CYAN}, {Fore.YELLOW}clear{Fore.CYAN}, {Fore.YELLOW}quit{Style.RESET_ALL}\n")

records = []

while True:
    message = input(f"{Fore.GREEN}Your text: {Style.RESET_ALL}").strip()

    if message == "":
        print(f"{Fore.RED}Please enter a sentence.{Style.RESET_ALL}")
        continue

    command = message.lower()

    if command == "quit":
        print(f"{Fore.BLUE}Thank you for using Mood Analyzer. Goodbye, {name}!{Style.RESET_ALL}")
        break

    elif command == "clear":
        records.clear()
        print(f"{Fore.CYAN}History has been cleared.{Style.RESET_ALL}")
        continue

    elif command == "history":
        if len(records) == 0:
            print(f"{Fore.YELLOW}No previous records found.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Previous Results:{Style.RESET_ALL}")
            for i, (text, score, mood) in enumerate(records, start=1):
                if mood == "Positive":
                    clr = Fore.GREEN
                elif mood == "Negative":
                    clr = Fore.RED
                else:
                    clr = Fore.YELLOW

                print(f"{i}. {clr}{text} | Score: {score:.2f} | {mood}{Style.RESET_ALL}")
        continue

    analysis = TextBlob(message)
    score = analysis.sentiment.polarity

    if score > 0.2:
        mood = "Positive"
        clr = Fore.GREEN
    elif score < -0.2:
        mood = "Negative"
        clr = Fore.RED
    else:
        mood = "Neutral"
        clr = Fore.YELLOW

    records.append((message, score, mood))

    print(f"{clr}Detected Sentiment: {mood}")
    print(f"Polarity Score: {score:.2f}{Style.RESET_ALL}")
