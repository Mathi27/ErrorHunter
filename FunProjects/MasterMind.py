
'''A low-level implementation of the classic game “Mastermind”. We need to write a program that generates a four-digit random 
code and the user needs to guess the code in 10 tries or less. If any digit out of the guessed four-digit code is wrong, 
the computer should print out “B”. If the digit is correct but at the wrong place, the computer should print “Y”.
If both the digit and position is correct, the computer should print “R”'''                                                             
  
  
import random
def gen_code():  
    set_code = [] 
      
    for i in range(4):
         val = random.randint(0, 9)
         set_code.append(val) 
          
    return set_code 
      
 
def input_code():  
    code = input("Enter your four digit guess code: ") 
    return code 
  
  
 
def mastermind():  
      
    genCode = gen_code() 
    i = 0
      
    while i < 10: 
        result = "" 
        inputCode = [int(c) for c in input_code()] 
          
        if len(inputCode) != 4: 
            print("Enter only 4 digit number") 
            continue
          
        if inputCode == genCode: 
             print("You guessed it !", genCode) 
             break
              
        for element in inputCode: 
              
            if element in genCode: 
                  
                if inputCode.index(element) == genCode.index(element): 
                    result+="R"
                else: 
                    result+="Y"
            else: 
                result+="B"
        print(result) 
          
        i += 1
    else:     
        print("You ran out of trys !", genCode)     
          
          
# Driver Code 
mastermind()