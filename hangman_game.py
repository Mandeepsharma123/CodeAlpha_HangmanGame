import random

# List of predefined words
words = ["python", "apple", "school", "computer", "flower"]

# Select a random word
word = random.choice(words)

# Create blanks for the guessed word
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
incorrect_guesses = 0
max_attempts = 6

print("===== Welcome to Hangman Game =====")

while incorrect_guesses < max_attempts and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)
    print("Guessed letters:", guessed_letters)

    guess = input("Enter a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if letter is in the word
    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong!")
        incorrect_guesses += 1

# Final result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)