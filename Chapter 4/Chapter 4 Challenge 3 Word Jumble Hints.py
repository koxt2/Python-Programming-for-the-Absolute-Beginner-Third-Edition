# Python Programming for the Absolute Beginner, Third Edition
# Chapter 4, Challenge 3

# Improve "Word Jumble" so that each word is paired with a hint.
# The player should be able to see the hint if he or she is stuck.
# Add a scoring system that rewards players who solve a jumble without asking for the hint.

# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

#Hints
hint_python = "\nYour favourite programming language"
hint_jumble = "\nYour favourite word game"
hint_easy = "\n!Hard"
hint_difficult = "\n!Easy"
hint_answer = "\nQuestion"
hint_xylophone = "\nWooden instrument"

# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

#Do you want a hint?
decision = ("y", "n")
help_hint = ""
while help_hint not in decision:
    help_hint = input("\nDo you want a hint? y/n")

while help_hint:
    if help_hint == "n":
        break
    elif correct == "python":
        print(hint_python)
        break
    elif correct == "jumble":
        print(hint_jumble)
        break
    elif correct == "easy":
        print(hint_easy)
        break
    elif correct == "difficult":
        print(hint_difficult)
        break
    elif correct == "answer":
        print(hint_answer)
        break
    elif correct == "xylophone":
        print(hint_xylophone)
        break

#scoring
count = 0
score = 10

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ")
    count += 1

score = score - count

if guess == correct:
    print("\nThat's it!  You guessed it!")
    print("Out of a maximum of 10 points your score is", score)

if help_hint == "y":
    score_hinted = score/2
    print("...but you used the hint so your final score was docked", score/2, "points")        
    print("\nYour final score is", score_hinted)
        

print("\nThanks for playing.")

input("\n\nPress the enter key to exit.")
