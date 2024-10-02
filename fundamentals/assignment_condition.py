food_price = 100
time = int(input("give you time: "))

if((time>=10 and time<15) or ((time>=18 or time<21))):
    print("You will get 15 percentage discount")
else:
    print("No discount")