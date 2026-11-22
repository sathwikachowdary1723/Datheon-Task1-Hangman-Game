import random

# List of words for the game
words = ["python", "programming", "computer", "developer", "keyboard",
         "software", "technology", "internet", "science", "coding"]

# Hangman ASCII art stages
hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =======
    """
]


def play_hangman():
    secret_word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("================================")
    print("      HANGMAN WORD GAME")
    print("================================")
    print("Guess the hidden word!")
    print("You have 6 incorrect attempts.\n")

    while wrong_guesses < max_attempts:

        # Display hangman art
        print(hangman_stages[wrong_guesses])

        # Display the word with guessed letters
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        print("Remaining attempts:", max_attempts - wrong_guesses)

        # Get user input
        guess = input("\nEnter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.\n")
            continue

        # Check duplicate guess
        if guess in guessed_letters:
            print("You already guessed that letter. Try another!\n")
            continue

        guessed_letters.add(guess)

        # Check whether the letter is in the word
        if guess in secret_word:
            print("Correct guess!\n")
        else:
            wrong_guesses += 1
            print("Incorrect guess!\n")

        # Check for victory
        if all(letter in guessed_letters for letter in secret_word):
            print(hangman_stages[wrong_guesses])
            print("Word:", secret_word)
            print("\nCongratulations! You guessed the word!")
            print("You Win! 🎉")
            break

    # Check for defeat
    if wrong_guesses == max_attempts:
        print(hangman_stages[wrong_guesses])
        print("\nGame Over!")
        print("The correct word was:", secret_word)
        print("You Lose!")


# Start the game
if __name__ == "__main__":
    play_hangman()