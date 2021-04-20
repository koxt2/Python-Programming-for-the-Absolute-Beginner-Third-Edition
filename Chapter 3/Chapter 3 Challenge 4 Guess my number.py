# Python Programming for the Absolute Beginner, Third Edition
# Chapter 3, Challenge 4

# Here's a bigger challenge. Write a pseudocode for a program where the player and the computer trade places in the number guessing game.
# That is, thr player picks a random number between 1 and 100 that the computer has to guess. 
# Before you start, think about how you guess. If it goes well, try coding the game.

#Guess my number game

# Pseudocode
#
# Ask the player to choose a number between 1 and 100 for the computer to guess
# Set the full range of numbers as an available range for the computer to choose from
# Get the computer to guess the number
#   Print the number and state if it's right or wrong
#       If the computer gets it wrong
# 	    If it's low then tell the computer it's wrong and low
#	        Set the guess as the lowest number the computer can choose a random number from
#	        Increase the number of guesses the computer has to taken by 1
#	    If it's high then tell the computer it's wrong and high
#		Set the guess as the highest number the computer can choose a random number from
#		Increase the number of guesses the computer has to taken by 1
# 	If the computer gets it right
#		Tell the computer how many attempts it took
# End the game



#Set the counter to 0, user number to 0 and the range of numbers the computer can use to 1,100
import random
count = 0
number = None
guess_limit_lo = 1
guess_limit_hi = 100

#Set a number for the computer to guess
while number not in range(1,100):
    number = int(input("\nEnter a number between 1 and 100 for the computer to guess... "))

#The computer takes it's first guess
input("\nPress enter to hear the computer's guess...")
guess = random.randint(guess_limit_lo, guess_limit_hi)

#The computer gets it wrong
while guess != number:
    if guess < number:
        print("\nThe computer guessed", guess, "\nThis is low, try again.")
        input("Press enter for the computer's next guess")
        guess_limit_lo = guess+1
        guess = random.randint(guess_limit_lo, guess_limit_hi)
        count += 1
    elif guess > number:
        print("\nThe computer guessed", guess, "\nThis is too high, try again.")
        input("Press enter for the computer's next guess")
        guess_limit_hi = guess-1
        guess = random.randint(guess_limit_lo, guess_limit_hi)
        count += 1

#The computer got it right!
print("\nThe computer guessed right! It guessed your number is", number,)
print("It took the computer", count+1, "attempts to get it right!")
input("\nPress enter to end the game")
    
    
