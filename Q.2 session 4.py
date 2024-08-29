num1 = int(input('please enter num1: '))
num2 = int(input('please enter num2: '))
op = input('please enter the operation: ')

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
elif op == '%':
    print(num1 % num2)
else:
    print('syntax error')