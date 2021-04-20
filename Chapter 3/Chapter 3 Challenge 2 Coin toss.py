# Python Programming for the Absolute Beginner, Third Edition
# Chapter 3, Challenge 2

# Write a program that flips a coin 100 times and then tells you the number of heads and tails.

#Coin flip

import random

heads = 0
tails = 0
count = 0

while count <100:
    toss = random.randint(1,2)
    if toss == 1:
        heads +=1
        count +=1
    else:
        tails +=1
        count +=1

print("In", count, "tosses of a coin it landed on heads", heads, "times and tails", tails, "times!")
input("Press enter to end")
    

