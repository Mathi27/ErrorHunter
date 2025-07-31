import random

def play_game():
    print("Welcome to Guess the Number!")
    target = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1

            if guess < target:
                print("Too low!")
            elif guess > target:
                print("Too high!")
            else:
                print(f" Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print(" Invalid input! Please enter a number.")

while True:
    print("\nMenu:")
    print("1. Play Guess the Number")
    print("2. Exit") 

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        play_game()
    elif choice == "2":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice! Please enter 1 to play or 2 to exit.")
 
