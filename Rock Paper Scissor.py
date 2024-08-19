import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    """Prompt the user to choose rock, paper, or scissors."""
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    """Display the choices and the result of the game."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

def play_again():
    """Ask the user if they want to play another round."""
    while True:
        again = input("Do you want to play again? (yes/no): ").lower()
        if again in ['yes', 'no']:
            return again == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nCurrent Score: You {user_score} - {computer_score} Computer")
        
        if not play_again():
            print("Thanks for playing! Final Score:")
            print(f"You: {user_score}, Computer: {computer_score}")
            break

if __name__ == "__main__":
    play_game()
