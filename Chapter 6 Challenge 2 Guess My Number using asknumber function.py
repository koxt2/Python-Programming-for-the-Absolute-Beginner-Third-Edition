# Python Programming for the Absolute Beginner, Third Edition
# Chapter 6, Challenge 2

# Modify the Guess my Number game by reusing the function ask_number()
# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

# Dont understand the question!

"""def ask_number():
    response = None
    while response not in range(low, high):
        response = int(input(question))
    print("You entered a number in given range after", step, "attempts")    
    return response"""

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1
  
# guessing loop
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
            
    guess = int(input("Take a guess: "))
    tries += 1

print("You guessed it!  The number was", the_number)
print("And it only took you", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
