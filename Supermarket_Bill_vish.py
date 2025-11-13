
#--------------------SUPERMART BILL GENERATION----------------------------


#Generate a bill for a SUPERMARKET PURCHASE.
#The program should store the items and their prices in a list of tuples.
#It should then iterate over this list to print out each item along with its Price.
#Finally, Calculate and print the total cost of all the items.

#Sample input:--
#Project to generate supermarket bill

#initialization
#Project to generate supermarket bill

#initialization
option_1 = ''
option_2 = ''
total=0
cnt = 0
item_list = '''
    Rice        Rs 10/kg
    Sugar       Rs 8/kg
    Oil         Rs 30/liter
    Salt        Rs 25/kg
    Paneer      Rs 40/kg
    Maggie      Rs 12/pack
    Boost       Rs 200/bottle 
'''
item_db = {"rice":10,"sugar":8,"oil":30,"salt":25,"paneer":40,"maggie":12,"boost":200}
user_cart = []

#
cust_name = input("Enter your name: ")
option_1 = input("Press 1 for list or 2 to exit: ")

while option_1!= 2:
    if option_1 not in ('1','2'):
        print(f"Please select valid option of 1 or 2")
        option_1 = input("Press 1 for list or 2 to exit: ")
    elif option_1 == '1':
        print(f"Available Products \n {item_list}")
        option_2 = input("Please choose \n - 1 To make a purchase \n - 2 to exit: ")
        while option_2 != '2':
            print(f"option 2 - {option_2}")
            if option_2 not in ('1','2'):
                print(f"Please select valid option of 1 or 2")
                option_2 = input("Please choose - 1 To make a purchase \n -2 to exit: ")
            elif option_2 == '1':    
                user_item = input("Please enter the item: ").lower()
                if user_item in item_db:                   
                    user_qty = input("Enter the quantity: ")
                    if user_qty.isdigit:
                        itm_price = item_db[user_item] * int(user_qty)
                        user_cart.append((user_item,user_qty,item_db[user_item],itm_price))
                    else:
                        print("Please enter a valid quantity")
                        user_qty = input("Enter the quantity: ")  
                    option_2 = input("Please choose - 1 To continue shopping - 2 to exit: ")    
                else:
                    print(f"Item {user_item} is not available in store currently!")
                    option_2 = input("Please choose - 1 To make a purchase\n - 2 to exit: ")
            # else:   
            #     break     

        print("="*40 + " Pythonlife supermart " + "="*40)            
        print("="*40 + "\tHyderabad\t" + "="*38)
        print(f"* Customer Name: {cust_name}\t\t\t\t\t\t\t\t\t\t \t *" )
        print("-"*100)
        print("** S.No.\t\t Items\t\t\t Quantity\t\t Price\t\t\t **")
        print("-"*100)
        for i,j,l,k in user_cart:
            cnt+=1
            print(f"*  {cnt}\t \t\t {i} \t\t {j} \t\t\t\t {k} \t\t\t\t *")
            total+=k
        print("-"*60)
        print(f"*\t\t\t\t\t Total Amount: Rs {float(total)}")  
        tax_amt = total * .18       
        print(f"*\t\t\t\t\t\t\t   Tax Amount: Rs {round(float(tax_amt),2)} (18% tax)")                            
        print("-"*60)
        print(f"*\t\t\t\t\t Final Amount: Rs {round(float(total + tax_amt),2)}")  
        print("-"*60)
        print("*\t\t\t\t \t Thank you & Visit again!! \t\t\t\t\t *")
        print("-"*60)
        if option_2 == '2': 
            break    
    else:
        break    
print(f"Thank you {cust_name} for shopping")