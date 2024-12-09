'''Infinite Monkey Theorem

The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, 
such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long would it take for a Python function
to generate just one sentence? The sentence we will go for is: “a computer science portal for geeks”. 

The way we will simulate this is to write a function that generates a string that is 35 characters long by choosing random letters from the 26 letters in the 
alphabet plus space. We will write another function that will score each generated string by comparing the randomly generated string to the goal. 
A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done.
If the letters are not correct then we will generate a whole new string. 

To make it easier to follow, our program should keep track of the best string generated so far.

'''
import random 
  
  
# function to generate  
# a random string  
def generateOne(strlen):  
      
    # string with all the alphabets 
    # and a space 
    alphabet = "abcdefghijklmnopqrstuvwxyz " 
    res ="" 
      
    for i in range(strlen): 
        res+= alphabet[random.randrange(27)] 
          
    return res 
  
# function to determine the  
# score of the generated string 
def score(goal, testString):  
    numSame = 0
      
    for i in range(len(goal)): 
        if goal[i] == testString[i]: 
            numSame+= 1
             
    return numSame % len(goal) 
 
def main():  
    goalString = "Open Source Day 2024 "
    newString = generateOne(35) 
    best = 0
    newScore = score(goalString, newString) 
      
    while newScore<=1: 
        if newScore >= best: 
            print(newString) 
            best = newScore 
        newString = generateOne(35) 
        newScore = score(goalString, newString) 
  
# Driver code 
main()