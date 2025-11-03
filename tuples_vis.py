#------------Tuples---------------
#create a tuple: Write a python that creates a tuple containing three elements:Your name, your age, and your favorite colour.then print the tuple.

user_name =("Vishnu",23," Blue")
print(user_name)

#2. Access Tuple Elements: write a prohram that creates a tuple containing the days of the week. Then, print the third element of the tuple.

days_of_the_week = ("Sun","mon","Tues","wed","Thru","fri","sat")
print(f"the days of the week are:{days_of_the_week}")
print(f" the third element of the tuple is:{days_of_the_week[2]}")

#3.Tuple Concatentation: write a program that creates two tuples, one containing odd numbers from 1 to 5 and another containing even numbers from 2 to 6. 
#concatenate these two tuples and print the result.

odd_tuple =(1,3,5)
even_tuple =(2,4,6)
print(f" the concatenation of odd and even tuples is :{odd_tuple+even_tuple}")

#4.Tuple Unpacking :
# write a program that defines a tuple containing the dimensions of a rectangle(length and width). 
#then, unpack this tuple into two variables and calculate the area of the rectangle.

rectangle =(10,5)
length = rectangle[0]
width = rectangle[1]
area = length*width
print(f" the are of rectangle with length {length} and width {width} is : {area}")

#5. check if an element exists:
#write a program that checks if a given element exists in a tuple.

sample_tuple =(10,20,343,35)
element_to_check = 343
if element_to_check in sample_tuple:
    print(f"{element_to_check} is present in the tuple")
else:
    print(f"{element_to_check} is not present in a tuple")

#6. Write a python program to generate a bill for a supermarket purchase. The program should store the items and their prices in a list of tuples.
#It should then iterate over this list to print out each item along with its price. Finally
#calculate and print the total cost of all the items.
items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
total = 0
print("Items\tprice")
print("-"*20)
for i,j in items:
    print(f"{i}\t{j}")
    total+=j
    print("-"*20)
    print(f"Total\t{total}")
print(f"Total\t{total}")
#---------------------------------

items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
total =0
print("-"*30)
print("\tItemized Bill")
print("-"*30)
print("\tItem\t Price")
print("-"*30)
for i,j in items:
    print(f"\t{i}\t {float(j)}")
    total+=j
print("-"*30)
print(f"\tTotal \t {float(total)}")
print("-"*30)
print("Thank you for shopping!!")
print("-"*30)
