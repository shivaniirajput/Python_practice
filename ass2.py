#perfect no.
val1 = int(input("enter the value"))
i=1
sum=0
while i!=int(1+val1/2):
    if val1%i==0:
        sum+=i
        i+=1
if sum==val1:
    print("no. is perfect")
else:
    print("no. is not perfect")

#occurence of cahr in string
st = input("enter any strng ")
ch = input("character to be searched ")
i=0
c = 0
while i!=len(st):
    if ch == st[i]:
        c+=1
        break
    i+=1
if c == 1:
    print("character found at location ",i+1)
else:
    print("cahracter not found")

#string anagrams

str1 = input('string 1: ')
str2 = input('string 2: ')
i=0
while i!=len(str1):
    count=0
    j=0
    while j!=len(str2):
        if str1[i] == str2[j]:
            count+=1
        j+=1
    if count==0:
        break
    i+=1
if count>0:
    print("strings are anagram")
else:
    print('strings are not anagram')

#vowel / consonent
ch2 = input("enter a character")
c=0
if ch2=='a' or ch2=='A':
    c+=1
elif ch2=='e' or ch2=='E':
    c+=1
elif ch2=='i' or ch2=='I':
    c+=1
elif ch2=='o' or ch2=='O':
    c+=1
elif ch2=='u' or ch2=='U':
    c+=1
else:
    c=0

if c>0:
    print("its a vowel")
else:
    print("its a consonenet")