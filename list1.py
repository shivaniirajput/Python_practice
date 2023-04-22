a = ["1" , "2"]
a[0] = "6"
print(a)                                    #replacing a number in list with another number

list1 = ["K" , "I" , "E" , "T"]
list1[1:3] = ["A" , "k"]                    #replacing a range of numbers with others       
print(list1)

list2 = ["B" , "I" , "J" , "N" , "O" , "R"]
list2.insert(2 , "insert1")                 #inserting new elements in a list by shifting other elements
print(list2)

list3 = ["1" , "2" , "3"]
list3.append("6")                           #to append an element in a list
print(list3)

list4 = ["1" , "2" , "3" , "4"]
list5 = ["5" , "6" , "7"]
list4.extend(list5)                         #to extend a list
print(list4)

list6 = ["1" , "2" , "3" , "4"]
list6.remove("1")                            #to remove an element from the list
print(list6)

list6.pop(0)                                 #to remove from an specified index
print(list6) 

list6.pop()                                   #remove value at 0 index by default
print(list6)                

list = ["10" , "20" , "30"]
del list                                      #delete a list completely 
print(list)      

list = ["0" , "1" , "2"]
list.clear()                                  #only delete the items from the list but not list
print(list)

#LOOPING THROUGH LIST
list = ["0" , "9" , "8"]
for x in list:
  print(x)

                 
