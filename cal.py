num1 = int(input('Enter your first num: '))
num2 = int(input('Enter your second num: '))

print('Choose your action: \n1.Add\n2.Subtract\n3.Multiply\n4.Divide')

while True:
    calculation = input('Please enter your action: ').lower()
    if calculation in ['add','subtract','multiply','divide']:
        break
    else:
        print('Please enter valid action')
 
if calculation=='add':
    num3=num1+num2
    print(f'Addition of {num1} and {num2} is {num3}')
elif calculation=='subtract':
    num3=num1-num2
    print(f'Subtraction of {num1} and {num2} is {num3}')
elif calculation=='multiply':
    num3=num1*num2
    print(f'Muliplication of {num1} and {num2} is {num3}')
elif calculation=='divide':
    if num2==0:
        print('Cannot divide by zero')
    else:
        num3=num1//num2
        print(f'Division of {num1} and {num2} is {num3}')
