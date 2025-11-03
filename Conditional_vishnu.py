#Conditional statements in python

#1. Vowel checker:
#write a python program that takes a character as input and checks whether it is a vowel or not.
#use the if-else statement.

# vowel_list = ['a','e','i','o','u']
# user_char = input("enter a character:")
# if(user_char in vowel_list):
#     print(f" the user entered character {user_char} is a vowel.")
# else:
#     print(f" the user entered character {user_char} is not a vowel.")

#2. Age group classification
#write a program that takes an age as input and classifies the person into 
#one of the following age groups:
# - Child (0-12)
# - Teenager (13-19)
# - Adult (20-64)
# - Senior (65 and above)

# age_input = int(input("please enter an age to know the age groups: "))
# if age_input <0 and age_input <=12:
#     print(f" the user entered age{age_input} falls under child ")
# elif age_input >=13 and age_input <=17:
#     print(f" the user entered age is {age_input} falls under teenager cateoger")
# elif age_input >=18 and age_input <64:
#     print(f" the user entered age is {age_input} falls under adult cateoger")
# elif age_input>=65:
#     print(f" the user entered age{age_input} falls under senior cateogery")
# else:
#     print(f" the user entred invalid value {age_input} enter age above 0")

#3. Number classifier:

#write a program that takes an age as input and classifies it as positive, 
# #negative, or zero. Use the 'if-elif0selse statement.

# number = int(input("enter a number"))
# if number > 0:
#     print(f" the number {number} is a positive:")
# elif number < 0:
#     print(f" the number {number} is a negative")
# else:
#     print(f" the number {number} is zero")

#4. Leap Year Checker:

#create a progrm that checks wheater a given year is a leap year or not.
#A leap year is divisible by 4, but bot by 100 unless it is divisbile by 400.

user_year = int(input("Enter the year: "))
if user_year%4==0:
    if user_year%100==0: 
        if user_year%400==0:
            print(f"""User entered year "{user_year}" is a leap year""")
        else:
            print(f"""User entered year "{user_year}" is not a leap year""")
    else:
        print(f"""User entered year "{user_year}" is a leap year""")
else:
    print(f"""User entered year "{user_year}" is not a leap year""")

#5.Calculator.
#Build a simple caluclator program that takes two numbers and an operator
#(+,-,*,/) as input and perfoms the corresponding operatio.

print("Calculator")
user_input_1 = int(input("Enter the first number"))      
user_input_2 = int(input("enter the second number "))
user_operator = input("""
 Enter the operation you want to perform: "/
                      "+" for adding,
                      "-" for subtracting
                      "*" for multiplication
                      "/" for dividing.
                      Enter your selection: """)
if user_operator=="+":
    print(f"""You selected "{user_operator}" for Adding. The sum of the two numbers {user_input_1} and {user_input_2} is {user_input_1 + user_input_2}""")
elif user_operator == "-":
    print(f"""You selected "{user_operator}" for Subtracting. The difference of the two numbers {user_input_1} and {user_input_2} is {user_input_1 - user_input_2}""")
elif user_operator == "*":
    print(f"""You selected "{user_operator}" for Multplying. The product of the two numbers {user_input_1} and {user_input_2} is {user_input_1 * user_input_2}""")
elif user_operator == "/":
    print(f"""You selected "{user_operator}" for Dividing. The division of the two numbers {user_input_1} and {user_input_2} is {user_input_1 / user_input_2}""")
else:
    print(f"""You selected an invalid operation "{user_operator}" """)                  

#Short Hand if:
#rewrite the following code using the short_hand
# if statement :
#inputs
#x = 8
# if x% 2 == 0: reslut = "even"
#else: result ="odd"

print("--------task Short Hand if-------")
x = 8
print(f""" short hand if condtion equivalent of given code is ""even" if x % 2 == 0 
      else "odd"" and its result is {"even" if x % 2 == 0 else "odd"} """)

#7.Discount Calulator:
#create a program that calculates the final price after applying a discount.
#the program should take the original price and
#  the discount percentage as input.

product_cost = float(input("Enter the product price: "))
discount_pct = (int(input("Enter the discount to be applied: "))) / 100
print(f"""The product cost is {product_cost} and discount to be applied is {discount_pct * 100}%. 
The final product price is {product_cost-(product_cost*discount_pct)}""")

#BMI Calculator.
#write a program that calculates the BODY mass index(BMI)
#using the formula: BMI = weight(kg) / height(m))^2.
#The program should tke weight nd height as input.

print("--------BMI Calulator---------")
user_weight = float(input("Please enter the weight in Kgs: "))
user_height_mt = float(input("Please enter the height meters: "))
print(f"""For a weight (kg) of "{user_weight}" and height (mt) of "{user_height_mt}" 
      The BMI calculates to "{round(user_weight / (user_height_mt ** 2),2)}" """)  

