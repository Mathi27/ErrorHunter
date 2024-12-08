'''Direction Catastrophe'''

'''A very simple problem with many different solutions, but the main aim is to solve it in the most efficient way. A man was given directions to go from point A to point B. The directions were: “SOUTH”, “NORTH”, “WEST”, “EAST”. Clearly “NORTH” and “SOUTH” are opposite, “WEST” and “EAST” too. Going to one direction and coming back in the opposite direction is a waste of time and energy. So, we need to help the man by writing a program that will eliminate the useless steps and will contain only the necessary directions. 
For example: The directions [“NORTH”, “SOUTH”, “SOUTH”, “EAST”, “WEST”, “NORTH”, “WEST”] should be reduced to [“WEST”]. This is because going “NORTH” and then immediately “SOUTH” means coming back to the same place. So we cancel them and we have [“SOUTH”, “EAST”, “WEST”, “NORTH”, “WEST”]. Next, we go “SOUTH”, take “EAST” and then immediately take “WEST”, which again means coming back to the same point. Hence we cancel “EAST” and “WEST” to giving us [“SOUTH”, “NORTH”, “WEST”]. It’s clear that “SOUTH” and “NORTH” are opposites hence canceled and finally we are left with [“WEST”].
'''

def reduce_dir(directions):
    opposite = {
        "EAST":  "WEST",
        "WEST":  "EAST",
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
     
    }
    stack = []
    for d in directions:
        if stack and opposite[d] == stack[-1]:
 
          
             
          
            stack.pop()
            
 
          stack.pop()
 
        else:
 
            stack.append(d)
    print(stack)
 
    return stack

dir = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
reduce_dir(dir)
 
    return stack

dir = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
reduce_dir(dir)
 
 
          stack.append(d)
    
    return stack

directions = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
result = reduce_dir(directions)
print(result)
 
 
