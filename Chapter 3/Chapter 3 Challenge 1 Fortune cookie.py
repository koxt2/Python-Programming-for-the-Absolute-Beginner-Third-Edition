# Python Programming for the Absolute Beginner, Third Edition
# Chapter 3, Challenge 1

# Write a program that simulates a fortune cookie. The program should display one of five unique fortunes, at random, each time it's run.

#Fortune cookie
import random

input("Press enter to open your forutne cookie!")

cookie = random.randint(1,5)
if cookie == 1:
    print("You are going to win the lottery on Saturday!")
elif cookie == 2:
        print("You are going to win the Euromillions on Friday!!")
elif cookie == 3:
        print("It will snow on Christmas Day!")
elif cookie == 4:
        print("The UK will leave the EU!!!")
elif cookie == 5:
        print("Aliens are going to land")
print("Press enter to end")




