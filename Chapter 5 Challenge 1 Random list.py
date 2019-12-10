# Python Programming for the Absolute Beginner, Third Edition
# Chapter 5, Challenge 1

# Create a program that prints a list of words in random order.
# The program should print all the words and not repeat any.

# Imports
import random

# Create list of words and a place for a new list
list = ["car", "phone", "house", "TV", "laptop"]
new = []

print("A list of words is", list)
input("Press enter to mix up the list")

# The loop
while list:
    word = random.choice(list)
    new.append(word)
    list.remove(word)

# Print new list
print("A mixed up version of the list is", new)


