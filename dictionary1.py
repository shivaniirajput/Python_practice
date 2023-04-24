dic = {
  "Name" : "Shivani",
  "Course" : "Btech",
  "Branch" : "CSE",
  "year" : 2023
}
print(dic)                                                       #printing a dictionary

dic = {
  "Name" : "Shivani",
  "Course" : "Btech",
  "Branch" : "CSE",
  "year" : 2023
}
print(dic["Name"])                                               #printing Name value in dictionary

dic = {
  "Name" : "Shivani",
  "Name" : "Shivu",                                              #same key can not have different value, the recent one override the previous one in case of same key
  "Branch" : "CSE",
  "year" : 2023
}
print(dic)    

dic = {
  "Name" : "Shivani",
  "Course" : "Btech",
  "Branch" : "CSE",
  "year" : 2023
}
print(len(dic))                                                 #printing number of items in diictionary

dic = {
  "Name" : "Shivani",
  "Course" : "Btech",
  "Branch" : "CSE",
  "year" : 2023,
  "Subjects" : ("OS", "MP"),
  "WEBD" : ["html" , "css" , "js"]
}
print(dic)                                                      #list and tuple data type can also be used as a value 

dic = {
  "Name" : "Shivani",
  "Course" : "Btech"

}
print(type(dic))                                                #printing data type i.e. dictrionary

dic = {
  "Name" : "Shivani",
  "Course" : "Btech"
 
}
x = dic.keys()                                                  #return all keys
print(x)

dic = {
  "Name" : "Shivani",
  "Course" : "Btech",
  "Branch" : "CSE",
  "year" : 2023
}
x = dic.keys()
print(x)                                                        #before adding a new key        

dic["Colour"] = "Black"
x = dic.keys()                                                  
print(x)                                                        #after adding a new key

dic = {
  "Name" : "Shivani",
  "Course" : "Btech"
 
}
x = dic.values()                                                  #return all values
print(x)

dic = {
  "Name" : "Shivani",
  "Course" : "Btech"
 
}
dic["Name"] = "Shiv"                                              #change key value
print(dic)

dic = {
  "Name" : "Shivani",
  "Course" : "Btech"
 
}
print(dic.pop("Name"))                                            #it will print pop value

dic = {
  "Name" : "Shivani",
  "Course" : "Btech"
 
}
dic.pop("Course")
print(dic)                                                        #print dictionary items after deleting specific element from it

dic = {
  "Name" : "Shivani",
  "Course" : "Btech"
 
}
dic.popitem()                                                     #delete last element from the dictionary
print(dic)

dic = {
  "Name" : "Shivani",
  "Course" : "Btech"
 
}
del dic["Name"]
print(dic)                                                       #delete specific element from dictionary

'''dic = {
  "Name" : "Shivani",
  "Course" : "Btech"
 
}
del dic
print(dic)                                                       #will generate error'''










                                           





  
  