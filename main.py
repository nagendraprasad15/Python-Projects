import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"

    if (user == "rock" and computer == "scissors") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissors" and computer == "paper"):
        return "You win!"

    return "Computer wins!"

def play_game():
    print("🎮 Rock Paper Scissors Game")
    print("Type 'exit' to quit\n")

    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()

        if user_choice == "exit":
            print("Thanks for playing!")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Try again.\n")
            continue

        computer_choice = get_computer_choice()

        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result + "\n")

if __name__ == "__main__":
    play_game()