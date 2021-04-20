# Python programming for the Absolute Beginner, Third Edition
# Chapter 2, Challenge 3

# Write a program where the user enters a restaurant bill total. The program should then display two amounts: a 15 percent tip and a 20 percent tip. 

#Calculate a tip
bill = float(input("What is the bill amount?: £"))
small_tip = str(round(bill*1.15, 2))
big_tip = str(round(bill*1.2, 2))
print("If you want to make a 15% tip then pay £" + small_tip, "but if you want to play a 20% tip pay £" + big_tip)

