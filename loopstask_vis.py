#-----------loops Tasks-----------
#Exercise 1:- Sum of Squares.
#write a program that calculates and prints the sum of the squares of numbers from 1 to 5 using a for loop.

sum_of_square = 0
for num in range(1,6):
    square_val = num ** 2
    print(f"""Square of {num} is {num ** 2}""")
    sum_of_square+=num ** 2

print(f"Sum of Squares of numbers 1 to 5 is {sum_of_square}")


#2. Countdown
#write a Python program that uses a
#while loop to print a countdownn from 5 to 1.

print("---------------------------while -------------------------------------------")
print("task - 2 - countdown from 5 to 1")
decr_counter = 5
print("countdown from 5 to 1 is:")
while decr_counter >= 1:
    print(f"{decr_counter}")
    decr_counter-=1
print("--------------while-----------------")


#3.multiplication table with nested for loop
#write a Python program to print the multiplication table for a user-specified number using a nested for loop.
print("----------------------------------------------------------------------------")
print("Multipilication table ")
table = int(input("Enter the table: "))
for i in range(1,11):
    print(f"{table} x {i} = table*i")

#4.Write  a python program that uses a "for" loop to find the sum of all even numbers between 0 to 10.

sum = 0
for i in range(0,11);
    if % 2==0:
        print(i)
        sum+=i
        print(f"sum of even numbers {sum}")

#.Cacluate the sum of all numbers from 1 to a given number.

num = int(input("enter the number: "))
sum = 0
for i in range(1,num+1):
    print(i)
    sum+=i
    print(f"sum of numbers {sum}")

#7.Display numbers from -10 to -1 using for loops.

for i in range(-10,-1):
    print(i)

#8.write a program to print the cube of all numbers from 1 to a given number.

numb= int(input("enter the number: "))
for i in range(1,numb+1):
    print(f" cube of {i} is {i**3}")
    