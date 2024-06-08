NAME-SHAHWAIZ SHAIKH 
BRACH-CO
BATCH-3

ASSIGNEMENT 1 -

while True:
    print('1 - dddition:')
    print('2 - subtraction:')
    print('3 - mulitiplication:')
    print('4 - division:')
    print('5 - exit')
    choice = input('enter choice:')
    if choice in ('1','2','3','4'):
        num1 = int(input("enter the first number:"))
        num2 = int(input("enter the second number:"))

        if choice =='1':
            print('addition:',(num1+num2))
        elif choice == '2':
            print('subtraction:',(num1-num2))
        elif choice == '3':
            print('mutiplication:',(num1*num2))
        elif choice == '4':
            print('division:',(num1/num2))
    elif choice == '5':
        break
    else:
        print('invalid input')

ASSIGNMENT 2-


i=0
while i==0:
    print('1 - celcius to farenheit')
    print('2 - farenheit to celcius')
    print('3 - exit')

    ch = input('enter choice')

    if ch in ('1','2'):
        temperature = float(input('enter temperature:'))

        if ch == '1':
            print('farenheit:',((temperature * 9/5)+32))
        elif ch == '2':
            print('celcius:',((temperature - 32)*5/9))
    elif ch == '3':
        i=1
    else:
        print('invaliad input')    


