#WAP TO USING SLICE OPERATOR
S = "KIET college Ghaziabad"
print(S[1:18:2])
print(S[-4:4:-1])
print(S[0:10:-2])                           #will not generate any output
print(S[::-2])
print(S[10:-4:1])

#WAP to access each character of string in forward and backward direction using while loop
S = "I am a CSE student"
i=0
while i<len(S):
  print(S[i])
  i+=1
  
i=(len(S)-1)
while i>=0:
  print(S[i])
  i=i-1
  
#WAP to reverse the given string(take input from user)
S = str(input("message"))
i = (len(S)-1)
while(i>=0):
  print(S[i])
  i = i-1

#WAP to perform the comparision operation between two string(taking input from user)
a = int(input("a"))
b = int(input("b"))
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)
print(a==b)
