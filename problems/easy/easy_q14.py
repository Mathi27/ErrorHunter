def vowel_or_consonant(char):
    char = char.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}

    if len(char) != 1 or not char.isalpha():
        return "Invalid input. Please enter a single alphabet letter."

    if char in vowels:
        return "Vowel"
    else:
        return "Consonant"

if __name__ == "__main__":
    characterInput = input("Enter a single alphabet character: ")
    result = vowel_or_consonant(characterInput)
    print("Result:", result)
