# Vowel or Consonant: Accept a character and use a switch case to determine if it is a vowel or a consonant.
def vowel_or_consonant(char):
    switch = {
        'a': "Vowel",
        'e': "Vowel",
        'i': "Vowel",
        'o': "Vowel",
        'u': "Vowel",
        'A': "Vowel",
        'E': "Vowel",
        'I': "Vowel",
        'O': "Vowel",
        'U': "Vowel"

    }
    if char in switch:
        return switch.get(char, "Vowel")   
    else:
        return "Consonant"
if __name__ == "__main__":
    characterInput  = input("Enter the charactrer : ")
    res = vowel_or_consonant(characterInput)
    print(res)
