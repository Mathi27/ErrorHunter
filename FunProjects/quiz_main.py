import time

def pause(seconds):
    time.sleep(seconds)

def ask_question(question):
    answer = input(question + "\nAnswer = ").strip().upper()  
    return answer

def evaluate_question(user_answer, correct_answer, alt_answer, close_answer):
   
    if user_answer == correct_answer:
        return False 
    elif user_answer in alt_answer:
        return False  
    elif user_answer in close_answer and close_answer:  
        return "Close"  
    else:
        return True  

def answer_response(evaluated):
    if evaluated == True:
        return "Oops! That's not the correct answer!"  
    elif evaluated == "Close":
        return "Close! But not quite right. Try again!"
    else:
        return "Correct! Well done."

correct_answers = 0
answer_index = 0  

questions = [
    "Solar power generates electricity from what source?",
    "Did the Apple iPhone first become available in 2005, 2006 or 2007?",
    "In terms of computing, what does CPU stand for?",
    "True or false? Nintendo was founded after the year 1900.",
    "The Hubble Space Telescope is named after which American astronomer?",
    "Is the wavelength of infrared light too long or short to be seen by humans?",
    "Firefox, Opera, Chrome, Safari and Explorer are types of what?",
    "True or false? Gold is not a good conductor of electricity?",
    "What science fiction writer wrote the three laws of robotics?",
    "Nano, Shuffle, Classic and Touch are variations of what?",
]

answers = [
    "THE SUN",
    "2007",
    "CENTRAL PROCESSING UNIT",
    "FALSE",
    "EDWIN HUBBLE",
    "LONG",
    "WEB BROWSER",
    "FALSE",
    "ISAAC ASIMOV",
    "IPOD"
]

alt_answers = [
    ["SUN"],
    ["TWO THOUSAND AND SEVEN"],
    [None],
    [None],
    ["EDWIN"],
    ["TOO LONG"],
    ["WEB BROWSERS", "BROWSER", "BROWSERS"],
    [None],
    ["ASIMOV"],
    ["THE APPLE IPOD", "APPLE IPOD", "THE IPOD"]
]

close_answers = [
    [None],
    [None],
    [None],
    [None],
    ["HUBBLE"],
    [None],
    ["PROGRAM", "COMPUTER PROGRAM", "PROGRAMS", "COMPUTER PROGRAMS"],
    [None],
    ["ISAAC"],
    [None]
]

close_responses = [
    None,
    None,
    None,
    None,
    "Hubble is the surname of the American astronomer that the Hubble Space Telescope was named after. Do you know the first name? I'll give you a clue, it begins with the letter E.",
    None,
    "Technically correct! However, do you know what type of computer programs they are?",
    None,
    "Isaac is the first name of the science fiction writer that wrote the three laws of robotics. Do you know his surname? I'll give you a clue, it begins with the letter A.",
    None
]

print("Welcome to Open Source Day Python Quiz.")
pause(2)
user_name = input("What is your name?\nName = ")
pause(1)
print("Hello, {}!".format(user_name))
pause(2)
print("Let's begin the quiz.")
pause(2)


for question in questions:
    answer = ask_question(question)
    evaluated = evaluate_question(answer, answers[answer_index], alt_answers[answer_index], close_answers[answer_index])

 
    while evaluated == "Close":
        pause(1)
        print(close_responses[answer_index]) 
        answer = ask_question(question)
        evaluated = evaluate_question(answer, answers[answer_index], alt_answers[answer_index], close_answers[answer_index])

   
    if evaluated == False:
        correct_answers += 1

   
    print(answer_response(evaluated))

    answer_index += 1  
    pause(2)


print(f"Thanks for taking this quiz, {user_name}.")
pause(2)


if correct_answers == 10:
    print("Congratulations, you got all 10 questions correct and have been awarded the gold medal!")
elif 10>correct_answers >=6:
    print(f"Congratulations, you got {correct_answers} questions correct and have been awarded the silver medal!")
elif 5>=correct_answers > 0:
    print(f"Congratulations, you got {correct_answers} questions correct and have been awarded the bronze medal!")
else:
    print("Take the quiz again to try and earn a gold medal!")



