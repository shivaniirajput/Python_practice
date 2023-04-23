cse = ["shiv" , "rohit" , "shivanu"]
csit = []

for x in cse:
  if "s" in x:
    csit.append(x)                             #using for loop to fliter elements and add into new list
    print(csit)
    
cse = ["shiv" , "shivani" , "rohit"]
csit = [x for x in cse if "a" in x]            #using list comprehension      
print(csit)

#LIST SORTING
list = ["apple" , "lichi" , "guava", "banana"]
list.sort()                                           #alphanumeric sorting
print(list)   

list = ["1" , "9" , "5" , "2"]
list.sort()
print(list)                                           #numeric sorting

list = ["apple" , "lichi" , "guava", "banana"]
list.sort(reverse = True)                             #alphanumeric sorting in descending order
print(list)  

list = ["1" , "9" , "5" , "2"]
list.sort(reverse = True)                            #numeric sorting in descending order
print(list) 

list = ["1" , "2" , "3"]
newList = list.copy()                               #copy elements of one list to another
print(newList)

list1 = ["python" , "c" , "c++"]
list2 = ["html" , "css" , "js"]
list = list1 + list2
print(list)     
    