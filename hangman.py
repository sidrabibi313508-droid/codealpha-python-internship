import random

# ── Predefined word list ──────────────────────────────────────────────────────
WORDS = ["python", "rocket", "jungle", "castle", "bridge"]

# ── Hangman ASCII stages (0 = safe … 6 = game over) ─────────────────────────
HANGMAN_STAGES = [
    """
   -----
   |   |
       |
       |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
       |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
   |   |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
========="""
]

MAX_WRONG = 6  # allowed incorrect guesses


def display_state(wrong_count, guessed_letters, secret_word):
    """Print the current hangman figure, blanks, and guessed letters."""
    print(HANGMAN_STAGES[wrong_count])
    print()

    # Show blanks / correctly guessed letters
    display = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    print("  Word:", display)
    print()

    # Show wrong guesses so far
    wrong_letters = sorted(
        letter for letter in guessed_letters
        if letter not in secret_word
    )
    if wrong_letters:
        print("  Wrong guesses:", ", ".join(wrong_letters))
    print(f"  Remaining attempts: {MAX_WRONG - wrong_count}")
    print()


def get_guess(guessed_letters):
    """Prompt the player for a valid, new single letter."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠  Please enter a single letter (a–z).")
        elif guess in guessed_letters:
            print(f"  ⚠  You already guessed '{guess}'. Try another.")
        else:
            return guess


def play_game():
    """Run one full round of Hangman."""
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_count = 0

    print("\n" + "=" * 40)
    print("        W E L C O M E  T O  H A N G M A N")
    print("=" * 40)
    print(f"\n  The secret word has {len(secret_word)} letters.")
    print(f"  You have {MAX_WRONG} incorrect guesses allowed.\n")

    # ── Main game loop ────────────────────────────────────────────────────────
    while True:
        display_state(wrong_count, guessed_letters, secret_word)

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            print("  🎉  You WON! The word was:", secret_word.upper())
            break

        # Check loss condition
        if wrong_count >= MAX_WRONG:
            print("  💀  Game over! The word was:", secret_word.upper())
            break

        # Get and process the player's guess
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"\n  ✅  '{guess}' is in the word!\n")
        else:
            wrong_count += 1
            print(f"\n  ❌  '{guess}' is NOT in the word.\n")


def main():
    """Entry point — supports replaying without restarting."""
    while True:
        play_game()
        print()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye. 👋\n")
            break


if __name__ == "__main__":
    main()
