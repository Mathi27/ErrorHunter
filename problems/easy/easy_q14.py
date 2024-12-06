# Vowel or Consonant: Accept a character and use a switch case to determine if it is a vowel or a consonant.
def vowel_or_consonant(char):
    switch = {
        'a': "Vowel",
        'e': "Vowel",
        'i': "Vowel",
        'o': "Vowel",
        'u': "Vowel",
    }
    return switch.get(char, "Not a Vowel: A Consonant")   #The default case is been modified to mean it is a consonant
if __name__ == "__main__":
    #the DataType of the input is changed to string
    characterInput  = input("Enter the charactrer : ").lower()
    res = vowel_or_consonant(characterInput)
    print(res)

# By: Deepak K M, 24UCS121, CSE_A