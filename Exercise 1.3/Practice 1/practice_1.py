first_number = int(input('Please give me your first number: '))
second_number = int(input(
    'Please give me your second number to be added or subracted from your first: '))
choose_operator = str(input('Please select and operator (+ or -): '))

if choose_operator == '-':
    print(first_number - second_number)

elif choose_operator == '+':
    print(first_number + second_number)

else:
    print('Unkown Operator')
