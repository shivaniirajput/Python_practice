#FUNCTIONS
def greetings_function():
  print('welcome folks')
  
greetings_function()

def greetings_function(name):
  print('welcome' + name)
  
greetings_function(' shivani ')

def personal_details(name , age ):
  print('My name is' + name + ' and I am '+ str(age) + ' years old')
  
personal_details('shivani' , 23)

def greetings_function(*names):
  print('welcome  ' + names[1])
  
greetings_function('ram' , 'shyam' , 'ramesh')

def personal_details(name , age ):
  print('My name is ' + name + ' and I am '+ str(age) + ' years old')

name = input('enter your name :')
age = input('enter your age :')  
personal_details(name , age)


  
  

