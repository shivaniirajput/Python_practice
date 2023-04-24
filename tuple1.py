tuple = ("1" , "2" , "3")
print(tuple)      

print(len(tuple))                                            #number of elements  in tuple

print(type(tuple))                                           #to print the data type

tuple1 = ("1" , "2" , "3", "python", "java")
print(tuple1[1])                                             #access tuple elements by index number
print(tuple1[2:4])                                           #access tuple elements by range
print(tuple1[:3])
print(tuple1[3:])

#updating tuple

'''x = ("1" , "2" , "3" , "4")
y = list(x)
y[0] = "0"                                                    #vs ne dhokha dediya
x = tuple(y)
print(x))'''

#LOOP
tuple1 = ("P" , "Y" , "T" , "H" , "O" , "N")
for x in tuple1:                                               #print all the items of tuple
  print(x)

tuple1 = ("m" , "o" , "n", "k" , "e" , "y")  
for i in range(len(tuple1)):                                   #printing tuple elements by index 
  print(tuple1[i])
  
#join tuples
tup1 = ("1" , "2" , "3")
tup2 = ("3" , "4" , "5")
tpp = tup1 + tup2                                              #join two tuples
print(tpp) 
