#Exercise 1:Write a Python program to calculate the area of a rectangle 
# using the given formula: area = length * width . Take the values of 
# length and width as inputs from the user.
print("please enter the length of the rectangle")
length = float(input())

print("please enter the width of the rectangle")
width = float(input())

area = length * width
print(f"Rectangle's length entered is {length} and width entered is {width}, the calculated are is {area} ")

#  Exercise 2: Write a Python program to demonstrate incrementing 
# and decrementing a variable 
print("Please enter a number to be incremented by 5")
incr_input = int(input())
incr_value = incr_input + 5 
print(f"Value to be incremented by 5 is {incr_input} and incremented value is {incr_value}")

print("please enter a number to decrement by 5")
decr_input = int(input())
decr_value = decr_input - 5 
print(f"Value to be decremented by 5 is {decr_input} and incremented value is {decr_value}")

# Exercise 3: Write a Python program to convert temperature from 
# Celsius to Fahrenheit. The formula for conversion is: F = (C * 9/5) + 32 . 
# Take the temperature in Celsius as input from the user.
print("please enter the temperture in celsius")
temp_in_celsius = float(input())
temp_in_fahrenheit = (temp_in_celsius * 9/5) + 32

print(f"The temp in celsius is {temp_in_celsius} converted to farheneit is {temp_in_fahrenheit}")


#  Exercise 4: Write a Python program to calculate the 
# simple interest given the principal amount, rate, and time (in years). 
print("please enter the principal amount")
principal_amt = float(input())
print("please enter the rate of interest")
rate = float(input())
print("enter the duration in years")
time = float(input())
simple_intrest = (principal_amt * rate * time) / 100
print(f"simple interest computed is {simple_intrest} ")


# Exercise 5: Write a Python program to concatenate two strings and display the result.
# The strings should be taken as input from the user. 
print("enter the first name")
fname = input()
print("enter last name")
lname = input()

print(f"first name entered is {fname} and last name entered is {lname} and full name is {fname + lname}")

# Exercise 6: Write a Python program to convert a distance from kilometers to miles
print("enter the distance in kilometer")
dist_km = float(input())
dist_mile = dist_km * 0.621371
print(f"distance in KM is {dist_km} and converted to miles is {dist_mile}")

# Exercise 7: Create a program that takes user input for # their name and age. 
# Use formatted strings (f-strings) to print a message welcoming the user and 
# stating their age. 
print("please enter your name") 
input_name = input()

print("please enter you age")
input_age= int(input())

print(f"Hello {input_name}, you mentioned that your age is {input_age}")

# Exercise 8: Create a list called numbers that contains integers from 1 to 10.
# 1: Check if the number 5 is in the list.
# 2: Check if the number 15 is not in the list
number_list = [1,2,3,4,5,6,7,8,9,10]
print(f"does list  {number_list} contain number 5 - {5 in number_list}")
print(f"does list {number_list} not contain number 15 - {15 not in number_list}")
