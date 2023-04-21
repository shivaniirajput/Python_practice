#DATA TYPE
#getting data type
a = 4
b = " okey "
c = [" my ", " name " , " is "]
d = (" my ", " name ", " is ")
print(type(a))    #will return integer data type
print(type(b))    ##will return string data type
print(type(c))    ##will return list
print(type(d))    ##will return tuple

#NUMBER
#type conversion
x = 2         #integer
y = 3.0       #float
z = 2 + 3j    #complex

a = float(x)       #convert x into float
b = int (y)        #convert y into integer 
c = complex (x)    #convert x into complex number
d = complex (y)    #convert y into complex number

#complex numbers can not be coverted into any other data type
print(a)
print(b)
print(c)
print(d)
print(z)

#RANDOM
import random
print(random.randrange(100,200))  #it will print any random value from 100 to (200-1)
