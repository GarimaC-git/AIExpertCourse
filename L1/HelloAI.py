# AI Chat Assistant

print("Hi! I'm Smart AI. Let's have a quick chat.")

# Ask for the user's name
name = input("What's your name? ")

print(f"Hello, {name}! It's great to meet you.")

# Ask about their favorite subject
subject = input("Which subject do you enjoy the most? ")

print(f"{subject} sounds like an interesting subject.")

# Ask if they like coding
answer = input("Do you like coding? (yes/no): ").lower()

# Respond based on the user's answer
if answer == "yes":
    print("That's great! Keep learning and creating new projects.")
elif answer == "no":
    print("No problem. With practice, coding can become enjoyable.")
else:
    print("Thanks for sharing your thoughts.")

# End the conversation
print(f"It was nice talking to you, {name}. Have a great day!")