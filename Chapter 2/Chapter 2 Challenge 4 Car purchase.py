# Python programming for the Absolute Beginner, Third Edition
# Chapter 2, Challenge 4

# Write a Car Salesman program where the user enters the base price of a car. The program should add on a bunch of extra fees such as tax, licence, dealer prep and destination charge.
# Make tax and licence a percent of a base price. The other fees should be set values.
# Display the actual price of the car once all the extras are applied. 

#Car purchase
base_price = float(input("What is the base price of the car?"))
leather = 950
winter_pack = 2200
cruise = 750
carpet = 500
metallic = 900
total = base_price + leather + winter_pack + cruise + carpet + metallic
total_inc_vat = round(total * 1.2, 2)
print("With the extras the total price of your new car is", total)
print("Including VAT, the cost is", total_inc_vat)

