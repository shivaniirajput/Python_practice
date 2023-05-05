'''# identifier can be class name or function name or variable name
cash = 10
print(cash)
#_a = protected variable
#__a = private variable
#_a_= magic variable
#_m()_ = magic method
import keyword
print(keyword.kwlist)
s1 = input('enter ')
print(type(s1))
#33 reserve keywords in Python
#14 datatypes are in python
str = 'kiet'
print(str[0:2].upper(),str[2:])
print(str[0:2].upper()+str[2:])
print(str[:-1]+str[-1].upper())
str2 = 'kiet'+'college'
str3 = 'kiet '*2
print(str2)
print(str3)

#complex dtype in python
A = 2+6j
print(type(A))
B= 3+6j
print(A+B)
print(A*B)

#True = 1
#False = 0
ab = True
ba=False
print(ab+ba)
print(ab*ba)
print(True+True+True)

#dtype conversion
val1 = 90.20
print(int(val1))
print(int(ab))
print(float(ab))

#we can convert from any type to int/float except complex type
#if we want to convert str type into int/float type compulsory str should contain only int/float part with base 10
val2 = '1102'
print(int(val2))
print(float(val2))

print(complex(val1))
print(complex(False))                     #######important
print(complex(ab))                        #####

#bool functions
print(bool(10))
print(bool(0))
print(bool(-1))
print(bool('dfdf'))
print(bool(''))

a=5.0112
b=3
print(a//b) #gives both float and int values , int if both are int
print(a**b)
print(10//3)
print(10/3)
print(10.0//3)
print(10**3)
print("KIET" + "10")
print("KIET" *3)
print("KIET" > "college")
print(10<20<30)
print(10<20>30<40>70)
print(10<<2)
print(10>>2) #sir ka doubt hai
print(~5)
a = 10
b = 20
c =30 if a>b else 40 #check krlena khud se

#is operator >>>>compares address
a=100
b=100
c=200
print(a is b)
print(a is c)
#== compares the data stored in that address
print(a==b)
print(a==c)
print(id(a))
print(id(c))
str1 = 'KIET'
str2 = 'KIET'
str3 = 'iit'
print(str1 is str2)
print(str1 is str3)

#membership (search a alphabet or a word in a string)

print('K' in str1)
print('i' in str1)
print('KIET' in str1)


for i in range (6):
    print('joker')

for i in range (101):
    if i%2!=0:
        print(i)


#biggest of 3 no.s

a=[]
i=0
max = 0
while i!=3:
    val = int(input('enter value'))
    a.append(val)
    if max<a[i]:
        max=a[i]
    i+=1
print(max)

#digit to string

al = int(input('enter value'))
if int(al/10)==0:
    if al==1:
        print('one')
    elif al==2:
        print('two')
    elif al==3:
        print('three')
    elif al==4:
        print('four')
    elif al==5:
        print('five')
    elif al==6:
        print('six')
    elif al==7:
        print('seven')
    elif al==8:
        print('eight')
    else:
        print('nine')
else:
    print('no. > 10')

#sum of 1st n natural no.s

dig = int(input('enter value of n'))
sum=0
i=1
while i<=dig:
    sum+=i
    i+=1
print('sum = ',sum)
'''

'''
aaaaa
bbbbb
ccccc
ddddd


for i in range (4):
    print(chr(65+i)*4)
'''
'''
i=1
while i!=6:
    print("* "*i)
    i+=1

print()

i=6
while i!=0:
    print("* "*i)
    i-=1
print()

i=1
j=6
while i!=6:
    while j!=0:
        print(" "*j+"*"*i)
        j-=1
    i+=1
'''
    ################################################ 



#prime check
'''
n = int(input("enter a no."))
i = 1
if n==1 or n==2:
    print("no. is prime")
else:
    i=2
    count = 0
    while i<int(n/2):
        i+=1
        if(n%i==0):
            count+=1
            break
        else:
            continue
    if count == 0:
        print("no. is prime")
    else:
        print("no. is not prime")

n=5
k = n - 1
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i+1):
        print("* ", end="")
    print("\r")

row = 5
for i in range(1, row+1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()

for i in range(row-1,0, -1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()
'''

'''#armstrong

val1 = int(input("armstring value input"))
i=0
val=val1
while val!=0:
    val=int(val/10)
    i+=1
sum=0
val=val1
while val!=0:
    sum+=(val%10)**i
    val=int(val/10)
if sum == val1:
    print('no. is armstrong')
else:
    print('no. isnt armstrong')

#reverse a no.

val2 = int(input("enter no. to be reversed"))
new=0
while val2!=0:
    new = new+(val2%10)
    val2 = int(val2/10)
    if val2!=0:
        new*=10
print("reversed ",new)

#factorial of a no.

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
val3 = int(input("fact value "))
print("factorial is ",fact(val3))

#convert decimal to binary, decimal to octal, decimal to hexadecimal

val4 = int(input('enter decimal value '))
print('binary value is')
n=0
while val4!=0:
    n=n+val4%2
    val4 = int(val4/2)
    if val4!=0:
        n*=10
print(n)'''

'''s = 'KIET college Ghaziabad'
print(s[1:10:2]) #slice ---+ve forward -ve backward
print(s[12:4:-2])
print(s[-5:8:-3])
print(s[::-1])
#print(s[10:4:0]) #slice cannot be 0
print(s[1:10])
print(s[:10])
print(s[7:])
print(s[:])'''
'''NOTEs()
if slice is -ve or +ve
-ve->+1 in end
+ve->-1 in end'''


#note that if we compare two strings then ASCII value is compared

#rstrip() removes spaces from right side
#lstrip() removes spaces from left
#strip removes spaces from both sidess 
s = "learning python is very easy"
#find() is used to find the location of an alphabet
print(s.find("r"))
print(s.find("python"))

#rfind() is used to find the location of an alphabet from right side
print(s.rfind("r"))

#count() is used to count the repeatation of a number
print(s.count("r"))
print(s.count('r',5,24))

print(s.replace('r','e'))                                               #replace() is used to replace an alphabet with another
