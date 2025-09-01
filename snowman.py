import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Show the current snowman stage
    print(STAGES[mistakes])

    # Show the secret word with underscores for unguessed letters
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    # Show the initial state of the snowman
    display_game_state(mistakes, secret_word, guessed_letters)

    # Prompt the user for one guess (we’ll expand later)
    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)
    print("You guessed:", guess)

    # Show updated state for testing
    mistakes = 1  # simulate one mistake for now
    display_game_state(mistakes, secret_word, guessed_letters)


if __name__ == "__main__":
    play_game()