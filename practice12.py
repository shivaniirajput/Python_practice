#reverse using for
st = input("enter string: ")
x = len(st)-1
for i in range (x,-1,-1):
    print(st[i],end="")
print()
#reverse using while
i=len(st)-1
while i>=0:
    print(st[i],end="")
    i-=1
print()
#using slice operator
print(st[-1:(-1)*(len(st)+1):-1])

# print Character at odd position and Even position
s = input("Enter string: ")
l = len(s)

print("even position characters: ")
for i in range(0,l):
  if i%2==0:
    print(s[i])

print("odd position characters: ")    
for i in range(0,l):
  if i%2!=0:
    print(s[i])
    
    
# merge character of string into a single string 
s1 = input("enter first string: ")
s2 = input("enter second string: ")

s = str(s1)+str(s2) 
print(s)   

# find the output given by using two string
#a) S1="KIET"

#b) S2="College"

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


    



  


