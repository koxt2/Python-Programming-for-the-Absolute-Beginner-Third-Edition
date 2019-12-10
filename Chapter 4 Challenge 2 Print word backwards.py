# Python Programming for the Absolute Beginner, Third Edition
# Chapter 4, Challenge 2

# Create a program that gets a message from the user and then prints it out backwards.

#Print word backwards
message = input("Enter a message: ")
new_message = ""
while message:
    position = len(message)
    new_message = message[position-1]
    message = message[:position-1]
    print(new_message, end = " ")
