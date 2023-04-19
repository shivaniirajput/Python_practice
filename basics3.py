#python casting
x = int(10.2) 
y = float(3)
z = str(4)

print(x)
print(y)
print(z)

#looping through a string
for x in "shivani":
  print(x)
  
#finding length of a string
y = "this is CSIT department"
print(len(y))

#check string
z = "let's do it"
print("d" in z)             #checking if yess
if "d" in z:
  print("yess , 'd' is present.")
  
  print("d" not in z)       #checking if not present
  
  
#SLICING
a = "Python lab"
print(a[1:5])           #it will print all the strings between 1 to 5 excluding 1 and 5
 
print(a[4:])            #will print all the strings after a[4] index or using slice to the end
print(a[-4:-1])         #negative indexing

a = "PYthon"
print(a.upper())        #to convert in upper case
print(a.lower())        #to convert in lower case

a = " hello world "
print(a.strip())                 #remove whitespace from beginning and end
print(a.replace("e" , "E"))      #replace a string with another
print(a.split())                 #returns ['hello' , 'world']

#string concatenation
a = "Shivani"
b = "Rajput"
c = a + b
print(c)                         #returns ShivaniRajput
c = a + " " + b
print(c)                         #returns Shivani Rajput

#format string to concatenate string with integer
a = 1
c = 20
d = 5
e = "my JEE rank is{} and i am {} years old and i have{} laptops"
b = "my JEE rank is {} "
print(b.format(a))               #returns my JEE rank is 1
print(e.format(a,c,d))           




               