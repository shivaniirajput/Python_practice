#LIST METHODS
list1 = [10,2,0,4,1]
list2 = ['banana' , 'apples' , 'mangos' , 'oranges' , 'lichi']
list2.append('cherry')
list1.insert(1,10)             #insert list element at specific position
list1.extend(list2)
print(list1)
print(len(list2))
print(list2.index('lichi'))
print(list2.count('mangos'))

