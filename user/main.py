again= 'yes'
while again=='yes':

 question= input ('Ask a question: ')


 from random import randint
 number= (randint(0, 4))


 if number == 1:
  print ('Yes')
 if number ==2:
  print ('No')
 if number== 3:  
  print ('Maybe')
 if number== 4:
  print ('Ask again later')
 
 again= input('would you like to go again?')
 
 while again== 'no':
   print('goodbye')