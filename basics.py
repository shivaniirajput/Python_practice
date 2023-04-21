#indentation
if 5 > 2:
  print("Five is greater than two.")
  
#creating variables
a = 10
b = "shivani"

#printing value of a and b
print(a)
print(b)

#using different values in one variable
x = 2
x = "Rajput"

#printing 
print(x)


#casting
r = int(3)
s = str(3)
t = float(3)

print(r)
print(s)
print(t)

#get the data type 
print(type(x)) #integer
print(type(b)) #string

#single and double quotes are same 
l = "shivu" 
m = 'shivu'
print(l)
print(m)

#case sensitive(both g and G will act different here)
g = 7
G = 9
print(g)
print(G)  #G will not override g

#many value to mutiple variables at one time
e , f , h = "mum" , "papa" , "world"
print(e)
print(f)
print(h)

#one value to multiple variables
u = v = w = "mine"
print(u)
print(v)
print(w)

#unpack a collection
college = ["books" , "laptop" , "placement"] #we have collection of values in a list
m , n , o = college   #extracting the values into different variables
print(m)  #printing seperatelly or unpack
print(n)  #printing seperatelly
print(o)  #printing seperatelly

#output multiple values 
a = " my "
b = " name "
c = " is "
d = " shivani "
e = " rajput "
f = 3
g = 5
print( a + b + c + d + e )   #priting all the values in same sequence
print( f + g )     #simple add if integer values are given
#print( a + f )     #not possible , will generate error

#global variables
x = 3

def myfunc():
  global x

  x = 5
  print(x)
  
myfunc()
print(x)  





  
  
