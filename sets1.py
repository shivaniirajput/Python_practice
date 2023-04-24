s = {"1" , "2" , "3"}
print(s)                                                            #printing set elements

s = {"1" , "2" , "1"}
print(s)                                                            #it will ignore duplicate values in set

s = {1 , "ramesh" , "geeta" , True}                                 #it considers 1 and True as a same value
print(s)

s = {1 , 2, 3 ,4}
print(len(s))                                                       #will print length of set

s = {1,2,2,3}
print(type(s))                                                      #will print set data type

s = {1,2,3,4}
for x in s:                                                         #printing set values one by one
  print(x)

s = {1 , 2 , 3}
print("1" in s)                                                     #return false
print(1 in s)                                                       #return true

s1 = {1 , 2 , 3}
s1.add(5)                                                           #add value in set
print(s1)

s1 = {1,2,3,4,5}
s2 = {6,7,8,9,0}
s2.update(s1)                                                       #adding element of one set into another
print(s2)

s1 = {1,2,3,4}
l1 = ["1" , "2"]
s1.update(l1)                                                       #adding list items to a set
print(s1)

s = {1 , 2 , 3 , 4}
s.remove(1)                                                         #to remove specific value from a set
print(s)                                                            #both remove and discard can be use to remove an item from a set bt if item is to be removes is not present in set remove throgh an error bt discard does not thrigh any error

s = {1,2,3,4,5}
s.pop()                                                             #by using pop any random item can be removed
print(s)

s = {1,2,3,4,5}
s.clear()                                                           #it empty the set
print(s)

s1 = {1,2,3,4}
s2 = {'a' , 'b'}
s3 = s1.union(s2)                                                   #union of two sets
print(s3)

s1 = {1,2,3,4}
s2 = {0,9,8}
s1.update(s2)                                                       
print(s1)

s1 = {1,2,3,4}
s2 = {2,3,7,8}
s1.intersection_update(s2)                                         #intersection
print(s1)

s1 = {1,2,3,4}
s2 = {1,7,2,6}
s = s1.intersection(s2)                                            #intersection
print(s)

