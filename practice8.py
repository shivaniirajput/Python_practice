#if statement
a = 4
b = 3

if a>b:
  print(str(a) + ' is greater than ' + str(b))

a = int(input('enter value of a : '))
b = int(input('enter value of b : '))

if a>b:
  print('a is greater than b')
  
elif a<b:
  print('a is less than b')
  

else:
  print('a is equal to b')
  
a = input('enter the value of a : ')

if type(a) == str:
  print(a + ' is a string ')
  
elif type(a) == int:
  print(a + ' is an integer')
  
elif type(a) == list:
  print(a + ' is a list')

elif type(a) == tuple:
  print(a + ' is a tuple')
  
else:
  print('we do not know the data type of a')
  
#check if a number is divided by 5 or not
num = int(input('enter the number: '))

if num%5==0:
  print(num , 'is divisible by 5')
else:
  print(num, 'is not divisible by 5')  