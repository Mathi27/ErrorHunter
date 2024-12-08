# Vowel or Consonant: Accept a character and use a switch case to determine if it is a vowel or a consonant.
def vowel_or_consonant(char):
    switch = {
        'a': "Vowel",
        'e': "Vowel",
        'i': "Vowel",
        'o': "Vowel",
        'u': "Vowel",
    }
    return switch.get(char.lower(),"Constant")   
if __name__ == "__main__":
    while True:
        characterInput  = input("Enter the charactrer : ")
        if len(characterInput)==1:
            result = vowel_or_consonant(characterInput)
            print(result)
        else:
            print("Please enter exactly one character.")