import random

def hangman():
    # Game setup
    words = ["Python", "Java", "C programming", "Java Script", "Ruby", "Sql"]
    word = random.choice(words).lower()
    max_attempts = 6
    incorrect_guesses = []
    progress = ["_"] * len(word)
    
    # ASCII art for hangman stages
    stages = [
        """
        -----
        |   |
            |
            |
            |
            |
        --------
        """,
        """
        -----
        |   |
        O   |
            |
            |
            |
        --------
        """,
        """
        -----
        |   |
        O   |
        |   |
            |
            |
        --------
        """,
        """
        -----
        |   |
        O   |
       /|   |
            |
            |
        --------
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
            |
            |
        --------
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
       /    |
            |
        --------
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        --------
        """
    ]

    print("Welcome to Computer languages Name Guess Game!")
    print(stages[0])
    print(" ".join(progress))

    while True:
        guess = input("Guess a letter: ").lower()
        
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
            
        if guess in incorrect_guesses or guess in progress:
            print("You already guessed that letter!")
            continue

        # Check guess
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    progress[i] = guess
            print("Correct guess  the next Word !")
        else:
            incorrect_guesses.append(guess)
            print(f"Wrong! Attempts left: {max_attempts - len(incorrect_guesses)}")
            print(stages[len(incorrect_guesses)])
            
        # Update display
        print(" ".join(progress))
        print("Incorrect guesses:", " ".join(incorrect_guesses))
        
        # Check win/lose conditions
        if "_" not in progress:
            print("Congratulations! You won !")
            break
        if len(incorrect_guesses) >= max_attempts:
            print(f"Game over! The word was: {word}")
            break

if __name__ == "__main__":
    hangman()