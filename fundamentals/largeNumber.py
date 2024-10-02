number_1=int(input('enter a number 1='))
number_2=int(input('enter a number 2='))
number_3=int(input('enter a number 3='))
number_4=int(input('enter a number 4='))
if (number_1>number_2 and number_1>number_3 and number_1>number_4):
    print('number_1 is maximum')
elif(number_2>number_1 and number_2>number_3 and number_2>number_4):
    print('number_2 is maximum')
elif(number_3>number_1 and number_3>number_4 and number_3>number_4):
    print('number_3 is maximum')
elif(number_4>number_1 and number_4>number_2 and number_4>number_3):
    print('number_4 is maximum')
else:
    print('all number are equal')


