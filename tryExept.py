try:
  a = int(input('Input an integer value: '))
  print(a)
  
except:
  print('OOPS......there is an error in printing your message')
  
else:
  print('nothing went wrong')
finally:
  print('try' ,'except' , 'finished')