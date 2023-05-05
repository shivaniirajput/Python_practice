#read file 
count_file = open(r"C:\Users\shiva\OneDrive\Desktop\PYTHON\count.txt")
#print(count_file.readlines())

for lines in count_file.readlines():
  print(lines)

count_file.close()