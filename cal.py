number1 = int(input('Enter your first number: '))
number2 = int(input('Enter your second numberber: '))

print('Choose your action: \n1.Add\n2.Subtract\n3.Multiply\n4.Divide')

while True:
    calculation = input('Please enter your action: ').lower()
    if calculation in ['add','subtract','multiply','divide']:
        break
    else:
        print('Please enter valid action')
 
if calculation=='add':
    number3=number1+number2
    print(f'Addition of {number1} and {number2} is {number3}')
elif calculation=='subtract':
    number3=number1-number2
    print(f'Subtraction of {number1} and {number2} is {number3}')
elif calculation=='multiply':
    number3=number1*number2
    print(f'Muliplication of {number1} and {number2} is {number3}')
elif calculation=='divide':
    if number2==0:
        print('Cannot divide by zero')
    else:
        number3=number1//number2
        print(f'Division of {number1} and {number2} is {number3}')
