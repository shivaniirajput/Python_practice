#creating a function
def func1 ():
  print("Hello ji") 

func1()                                                             #calling function func1

#function with arguement
def func1 (sName):
  print(sName , "Rajput")

func1("Shivani")
func1("Shivanu")
func1("Shivanya")

def func1(*color):
  print(color[0] , "is my favourite")                               
func1('black','kala')

def func1(color1,color2,color3,color4):
  print("My favourite colour is " + color3)
  
func1(color2 = "black" , color1 = "kala" , color3 = "kalota" , color4 = "kariya")

def func1(**color):
  print("Mera pasandida rang hai " + color["pasandida"])
func1(fav = "black" , pasandida = "kala")

def func1(color = "gora"):
  print("My favrouite colour is " + color)

func1("black")
func1("safed")
func1()
func1("bhoora")

def func1(food):
  for x in food:
    print(x)

khana = ["roti" , "sabji" , "chaval" , "aachar" , "salad"]

func1(khana)

def func1(x):
  return 2*x

print(func1(7))
print(func1(5))
print(func1(9))

