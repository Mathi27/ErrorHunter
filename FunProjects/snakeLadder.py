import random

def snake_and_ladder():
    position = 0
 
    while (position < 100):
 
    snakes = {25: 10, 40: 5, 90: 48} 
    ladders = {3: 22, 50: 75, 70: 89}  
    position = 0
    moves = 0

    print("Starting the game of Snake and Ladder!")
    print(f"snakes: {snakes}")
    print(f"Ladders: {ladders}")

    while position != 100:
        input("Press Enter to roll the dice...")
 
        dice = random.randint(1, 6)
 
        print(f"\nYou rolled: {dice}")
       
        
        # Check if the dice roll exceeds 100
        if position + dice > 100:
            print(f"Cannot move. Current Position: {position}")
            continue

        position += dice
 
        if position == 100:
            print("You won the game!!")
            break
        elif position == 50:  # Climbing a ladder
 
        if position + dice <= 100:  
            position += dice
        if position == 50:  
 
            position = 75
        elif position == 25:  
            position = 10
            
           
        print(f"Dice: {dice}, Position: {position}")
 
    else:
        print("You  are in the 100 th place YOU won the game" )
 
        
        # Check for snakes or ladders
        if position in snakes:
            print(f"Oops! Snake bite at {position}. Sliding down to {snakes[position]}")
            position = snakes[position]
        elif position in ladders:
            print(f"Yay! Ladder at {position}. Climbing up to {ladders[position]}")
            position = ladders[position]
 
        if position == 100:
            print("You won!!")
 

        print(f"Current Position: {position}")
    
    print("\nCongratulations! You reached position 100 and won the game!")
 
snake_and_ladder()
