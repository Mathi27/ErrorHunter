def hangman():
    word = "python"
    guessed = ["_"] * len(word)
    attempts = 7
    used_letters = set()

    print("Word to guess:", " ".join(guessed))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
        else:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Correct! Word:", " ".join(guessed))

        if "_" not in guessed:
            print("Congratulations! You guessed the word!")
            break
hangman()        
