#-------------------Transfer taks----------------------
#1. Using Break in a while Loop
#write a python program that takes a list of numbers as input = [25,30,20,40,15,25]
#and prints the sum of the numbers. However, if the sum exceeds 100,
#stop adding numbers and print "sum exceeded 100".



num = [25,30,20,40,15,25]
sum=0
i=0
for i in num:
    sum+=i
    if sum>100:
        break
print(f"sum exceeded 100 {sum}")

#2.using countinue in a for loop
#write a pyhthon script that uses a for loop to iterate through numbers from 1 to 600.
#print only the odd numbers, skipping the even ones using the continue statement.

number_list = 600
for i in range(1,number_list + 1):
    if i%2==0:
        continue
    print(f"odd numbers are {i}")

#3. using pass in conditional statements
#write a python script that checks if a number is even or odd.
#If the number is even, print "Even"; if odd, do nothing
#(using the pass statement).

numbers = int(input("Enter the numbers to check even or odd: "))
if numbers%2==0:
    print(f"number {numbers} is even ")
else:
    pass
print("odd number checker completed")


#4.combining trasfer statements
#write a python script that iterates through a list of words.
#if the worrd is "break", exit the loop using the break statement.
#if the word is "Skip", skip the rest of the code for the current iteratioin using the continue statement.
    #for any other word, print the word.

