#removing space 
s1 = "             kiet"
s2 = "kiet             "
s3 = "            kiet             "

print(s1.lstrip())
print(s2.rstrip())
print(s3.strip())

#using find()
s = 'Chalo bhaiya python pdh hi lete hein'
print(s.find("kiet"))
print(s.find("python"))
print(s.find("C"))

#using count function
s = "ababababababbabbbsbsbbsbsbabbabab"
print(s.count('a'))
print(s.count('b'))
print(s.count('s'))

#replace string with another string
s = 'I am a btech student'
print(s.replace("btech","medical"))

#upper case and lower case
s = "i am A BTECH student"
print(s.upper())
print(s.lower())
print(s.swapcase())

#using title to change every first letter to change in upper case
s = "i am a computer science student"
print(s.title())

print(s.capitalize())                              #change first alphabet of a sentence in upper case

