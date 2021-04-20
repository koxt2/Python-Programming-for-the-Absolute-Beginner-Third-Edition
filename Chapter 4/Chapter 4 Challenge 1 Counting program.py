# Python Programming for the Absolute Beginner, Third Edition
# Chapter 4, Challenge 1

# Write a program that counts for the user. 
# Let the user choose the starting number, ending number, and the amount by which to count.

# Choose the start, end and interval.
start = int(input("Enter a start number: "))
finish = int(input("Enter an end number: "))
interval = int(input("Enter the counting increments "))
for i in range(start, finish+1, interval):
    print (i)
