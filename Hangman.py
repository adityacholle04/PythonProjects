from Hangman_words import word_list
from Hangman_art import logo, stages
import random
from replit import clear

# Start With Logo
print(logo)

# Get word from all random list of words
chosen_word = random.choice(word_list)
print(chosen_word)

# Create list of word
word_len = len(chosen_word)
word = []
for i in range(word_len):
    word += '_'

# Flag for game end condition or win
end_game = False
lives = 6

while not end_game:
    clear()
    print(word)
    guess = input("Guess the letter:")
    for i in range(word_len):
        if guess == chosen_word[i]:
            word[i] = guess
            if '_' not in word:
                end_game = True
                print("You WIN")

    if guess not in chosen_word:
        lives -= 1
        print("You lost one live")

    print(stages[lives])

    if lives == 0:
        end_game = True
        print("You lost")
