import random

def snake_and_ladder():
    position = 0
    while position != 100:
        dice = random.randint(1, 6)
        if position + dice <= 100:  
            position += dice
        if position == 50:  
            position = 75
        elif position == 25:  
            position = 10
            
           
        print(f"Dice: {dice}, Position: {position}")
        if position == 100:
            print("You won!!")

snake_and_ladder()