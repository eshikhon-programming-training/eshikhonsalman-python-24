
name = input('Enter you name: ')
phone_number = input("enter you phone: ")
size_name = len(name)
size_phone = len(phone_number)
email = input('Enter you email: ')
size_email = len(email)

print(size_name)

if(size_name==0 or size_phone==0 or size_email==0):
    print("The field can not be empty")
else:
    if(size_name<3 or size_name>5):

        print("The name length must be between 3 and 5")
    elif(size_phone!=11):
        print("The phone length must be minimum 11")
    else:
        print("success")


# product_price = int(input("Enter your price: "))

# no_of_month = int(input("Enter you no of month: "))

# if(no_of_month==12):
#     final_price = product_price + (product_price*8)/100
# elif(no_of_month == 24):
#     final_price = product_price + (product_price*16)/100
# else:
#     print("Not Available")

# print(product_price)
# print(final_price/no_of_month)





