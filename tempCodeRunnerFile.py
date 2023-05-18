
s1 = input("enter first string: ")
s2 = input("enter second string: ")

x1 = len(s1)
x2 = len(s2)

x = 0
if x1>x2:
  x=x1

else:
  x=x2
  
i = 0
while i<x:
  if i<x1:
    print(s1[i] , end="")
  
  if i<x2:
    print(s2[i], end="")
    
  i+=1