# Vowel or Consonant: Accept a character and use a switch case to determine if it is a vowel or a consonant.
def vowel_or_consonant(char):
    if len(char) != 1 or not char.isalpha():
        return "Invalid input"
    char=char.lower()
    
    switch = {
        'a': "Vowel",
        'e': "Vowel",
        'i': "Vowel",
        'o': "Vowel",
        'u': "Vowel"
    }

    return switch.get(char, "Consonant")
if __name__ == "__main__":
    characterInput  = input("Enter the character : ")
 
    print(vowel_or_consonant(characterInput))

 
 
    