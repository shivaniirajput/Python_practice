'''class MyClass:
  x = 5
  
p1 = MyClass()
print(p1.x)'''

class person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
name = input('enter your name: ')
age = input('enter your age: ')
p1 = person(name,age)
#del p1.age will delete age from output
#del p1 will delete whole result
#pass : py using it a code pass the code without generating an error
print(p1.name) 
print(p1.age) 
