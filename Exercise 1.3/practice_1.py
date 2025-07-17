first_number = int(input('Please give me your first number: '))
second_number = int(input(
    'Please give me your second number to be added or subracted from your first: '))
choose_operator = str(input('Please select and operator '+' or '-': '))
math_problem = (first_number + choose_operator + second_number)
print(math_problem)
