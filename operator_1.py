#Arithmatic operators

x = 4
y =2 

print(x + y)     #addition of two numbers
print(x - y)     #subtraction of two numbers
print(x * y)     #multiplication of two numbers
print(x / y)     #divide two numbers
print(x % y)     #modulus of two numbers
print(x ** y)    #exponent value ie. x will multiply y times
print(x // y)    #floor division

#Assignment operator

x = 5

x += 3
print ( x )

x -= 3
print ( x )

x *= 3
print ( x )

x %= 3
print ( x )

x /= 3
print ( x )

x //= 3
print ( x )

x **= 3
print ( x )

#Comparision operator
x = 3
y = 5

print(x==y)
print(x>=y)
print(x<=y)
print(x!=y)
print(x > y)
print(x < y)

#Logical operator
x = 5
print(x>6 and x<4)
print(x<6 and x>4)
print(x<6 and x<4)
print(x<6 or x<4)
print(x<6 or x>4)
print(x>6 or x<4)
print(not(x<6 and x>4))
print(not(x>6 or x>4))

#Identity element
x = ["banana","apple"]
y = ["banana","apple"]
z = x
print(x)
print(y is x)               #return false because object or y and x are different
print(z is x)               #return true because object of z and x are same 

#Bitwise operator
x = 3
y = 5
print(x&y)                  #AND operation
print(x|y)                  #OR operation
print(x^y)                  #XOR operation
print(x>>y)                 #RIGHT SHIFT operation
print(x<<y)                 #LEFT SHIFT operation
print(~x)                   #NOT operation
print(~y)                   #NOT operation










