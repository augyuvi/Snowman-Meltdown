"""
game_logic.py
Contains the main Snowman game logic.
"""

import random
from ascii_art import STAGES

# List of words used in the game
WORDS = [
    "python",
    "git",
    "github",
    "snowman",
    "meltdown",
    "commit",
    "branch",
    "repository",
]


def get_random_word():
    """Pick and return a random word from WORDS."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display snowman stage and current word progress."""
    print("\n" + "=" * 30)
    print(STAGES[mistakes])  # show ASCII art

    display_word = " ".join(
        [letter if letter in guessed_letters else "_" for letter in secret_word]
    )
    print("Word:", display_word)
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print("=" * 30 + "\n")


def get_valid_guess(guessed_letters):
    """
    Ask the player for a single valid guess.
    - Must be a single alphabet character.
    - Must not be a repeat guess.
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Enter only a single letter (a-z).")
        elif guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
        else:
            return guess


def play_game():
    """Run one round of the Snowman game."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("❄️ Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 Congrats! You saved the snowman!")
            break

        if mistakes >= max_mistakes:
            print("💀 Oh no! The snowman melted!")
            print("The word was:", secret_word)
            break

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print("❌ Wrong guess!")
        else:
            print("✅ Correct guess!")


def play_with_replay():
    """Run the game, and ask if the player wants to replay."""
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("👋 Thanks for playing Snowman Meltdown!")
            break
