'''The substring dilemma

This is a really interesting program as it generates some really funny outputs. It is also a healthy practice problem for beginners 
who want to understand the “string” type more clearly. Let’s look into the problem.

Given a string, find a substring based on the following conditions: 

The substring must be the longest one of all the possible substring in the given string. 
There must not be any repeating characters in the substring. 
If there is more than one substring satisfying the above two conditions, then print the substring which occurs first. 
If there is no substring satisfying all the aforementioned conditions then print -1. 

'''
def test_1(string =""): 
      
     
    substring = ""  
    testList = [] 
    initial = 0
      
    for char in string: 
          
        for i in range(initial, len(string)): 
            substring+= string[i] 
              
             
            if substring.count(string[i])>=1: 
                testList.append(substring[:1-]) 
                initial+= 1
                substring = "" 
                break
    maxi ="" 
      
    for word in testList: 
          
        if len(word)>len(maxi): 
            maxi = word 
              
    if len(maxi)<=3: 
        return "-1"
    else: 
        return maxi 
      
 
print(test_1("character")) 
print(test_1("standfan")) 
# print(test_1("class"))