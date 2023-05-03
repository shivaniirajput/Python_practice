num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
operator = input('Enter operator : ')

if operator == '+':
  print('The addition is ' , num1 + num2)
  
elif operator == '-':
  print('The subtraction is ',num1 - num2)
  
elif operator == '*':
  print('The multiplication is ',num1 * num2)
  
elif operator == '/':
  print('The division is ',num1 / num2)
  
elif operator == '%':
  print('The remainder is ',num1 % num2)
  
else:
  print('Invalid operator')