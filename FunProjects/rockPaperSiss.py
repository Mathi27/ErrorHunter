import random
 
def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_choice == "quit":
            break
        if user_choice not in choices:
            print("Invalid choice! Try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")

def main():
    while True:
        print("\nMenu:")
        print("1. Play Rock, Paper, Scissors")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            rock_paper_scissors()
        elif choice == "2":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice! Please try again.")

main()