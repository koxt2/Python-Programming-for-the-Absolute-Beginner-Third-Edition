# Python Programming for the Absolute Beginner, Third Edition
# Chapter 3, Challenge 3

# Modify the Guess My Number game so that the player has a limited number of guesses.
# If the player fails to guesses in time, the program should display an appropriately chastising message.

# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("You only have 10 attempts\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != the_number and tries <= 10:
    if guess > the_number:
        print("Lower...")
        guess = int(input("Take a guess: "))
        tries += 1 
    else:
        print("Higher...")
        guess = int(input("Take a guess: "))
        tries += 1 

# End game
if guess == the_number:
    print("\nYou guessed it!  The number was", the_number)
    print("And it only took you", tries, "tries!\n")
else:
    print("\nToo many tries. Game Over!")

 
input("\n\nPress the enter key to exit.")
