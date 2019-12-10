# Python Programming for the Absolute Beginner, Third Edition
# Chapter 4, Challenge 4

# Create a game where the computer picks a random word and the player has to guess that word.
# The computer tells the player how many letters in the word.
# Then the player gets five chances to ask if a letter is in the word.
# The computer can only respond with "yes" or "no". Then the player must guess the word.
# I've added scoring and hints.

import random

# sequence of possible words
WORDS = ("computer", "book", "kitchen", "window", "galaxy", "television")
# computer selects a word
word = random.choice(WORDS)

# start the game

# how many letters are in the word?
letters = len(word)
print("\nThe computer has selected a word and it is", letters, "letters long")

# user guesses letters
count = 0
choices = ""
while count < 5:
    choice = input("Choose a letter and see if it's in the word: ")
    if choice in choices:
        print("You have already chosen that letter! Have another go for free")
        continue
    count += 1
    if choice.lower() in word:
        print("\nYes!", choice, "is in the word")
        choices += choice
    else:
        print("\nNo!,", choice, "is not in the word")
print("\n\nYou have had 5 chances to guess if a letter is in the word")
print("\nOut of your choices", len(choices), "are in the word")
print("\nThe word is", letters, "letters long and contains", choices)
print("Guess the word!: ")

# user guesses the word
#Hints
hint_computer = "\nPC"
hint_book = "\nCollection of text"
hint_kitchen = "\nFood prep area"
hint_window = "\n... shows the outside"
hint_galaxy = "\nMilky Way"
hint_television = "\nTV"
#Do you want a hint?
decision = ("y", "n")
help_hint = ""
while help_hint not in decision:
    help_hint = input("\nDo you want a hint? y/n")

while help_hint:
    if help_hint == "n":
        break
    elif word == "computer":
        print(hint_computer)
        break
    elif word == "book":
        print(hint_book)
        break
    elif word == "kitchen":
        print(hint_kitchen)
        break
    elif word == "galaxy":
        print(hint_galaxy)
        break
    elif word == "television":
        print(hint_television)
        break

#Guesses
attempts = 0
score = 10

guess = input("\nYour guess: ")
while guess != word and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ")
    attempts += 1

# scoring
score = score - attempts

if guess == word:
    print("\nThat's it!  You guessed it!")
    print("Out of a maximum of 10 points your score is", score)

if help_hint == "y":
    score_hinted = score/2
    print("...but you used the hint so your final score was docked", score/2, "points")        
    print("\nYour final score is", score_hinted)
        

print("\nThanks for playing.")

input("\n\nPress the enter key to exit.")
