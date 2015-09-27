

####*****1.  Get month and days for all months 

##months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'] 
##
##day = [31,28,31,30,31,30,31,31,30,31,30,31]
##
##i=0
##for i in range(0,12):
##   print 'Month ' + str(months[i]) + ' has ' + str(day[i])+ ' days'
##   i=i+1

##*****1. Given days in a month print out days

##day = [31,28,31,30,31,30,31,31,30,31,30,31]
##months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
##days= int(raw_input('Enter the days you are interested in i.e 28 days,30 days or 31 days: '))
##i=0
##if (days ==31 or days ==28 or days ==30) :
##    for i in range (0,12):
##      if day[i]== days:
##       print months[i] + ' has ' + str(days) + ' days'
##      i=i+1
##    
##else:    
##   print 'Please enter a valid number which are either 28, 30 or 31'   
####     

####**** Program to check hierarchy of if and elif statements 

##numbers = [ 1 , 3 , 5, 7 , 11 , 13 , 17 , 19 ] # this line creates a list of numbers
##numbers.sort() # this line will sort the list " Numbers", but its destructive, The original order(if any) of the list is lost
##
##nn = int(raw_input( 'new number : ' )) # this creates a new variable 'nn' and is assigned a value taken from the raw input. The input is converted to interger by the 'int' function before its assigned to 'nn'
##
##if nn in numbers : # (We will call this first condition) This line will check if the value assigned to variable 'nn'  is present in the the given list 'numbers' and if its found it will print 'tough luck'.
## print ' tough luck ' # if the condition mentioned in the above line is true then it will print out 'tough luck'
##elif nn > 20: # (We will call this Second condition) If the first condition fails, then we will come to the second condition  and if the value entered (nn) in the 3rd line is greater than 20 (second condition is true) then the below command will be executed
## numbers.append(nn) # if the above Second condition is satisfied then the value entered in the 3rd line will be appended to the sorted list of numbers and the below command will be executed
## print ' attached ' after appending the value of 'nn' to the numbers list this line will print 'attached'
##else: # if the if and elif fail (first and second condition fail)then the this condition will be executed and the below operations will be executed
## numbers.insert(0,nn) # this will insert the value assigned to 'nn' to the numbers list as a first element (index =0), displacing the subsequent element by +1 index   then will let the flow to the next line, it will not be in ascending order
## print ' f i r s t ! '   # after the above line (else condition) is executed  the systen will print 'First'


####****  Write a program to guess a number from a given range

##number = int(raw_input('Please think of a number from 1 to 20 : '))
##counter = 0
##
##if number > 0 and number < 21:
##  while counter <=3:
##    counter = counter +1
##    Question_1= (raw_input('Is the number greater than 10, please enter yes or no: '))
##    if Question_1 =='yes':
##          counter = counter +1
##          Question_2= (raw_input('Is the number even, please enter yes or no: '))
##          if Question_2 =='yes':
##              counter =   counter +1
##              Question_3= raw_input('Is the number greater than 16, please enter yes or no: ')
##              if Question_3 =='yes':
##                  counter = counter +1
##                  Question_4= raw_input('Is the number 18, please enter yes or no: ')
##                  if Question_4 == 'yes':
##                      print 'Mystic Forces have correctly predicted the number to be 18 and the guess count is ' + str(counter)
##                      break
##                  else:
##                      print 'Mystic Forces have correctly predicted the number to be 20 and the guess count is ' + str(counter)
##              elif Question_3 =='no':
##                   counter = counter +1
##                   Question_4= raw_input('Is the number 16, please enter yes or no: ')
##                   if Question_4 == 'yes':
##                      print 'Mystic Forces have correctly predicted the number to be 16 and the guess count is ' + str(counter)
##                      break
##                   else:
##                      print 'Mystic Forces have correctly predicted the number to be either 12 or 14 and the guess count is ' + str(counter)
##
##
##
##          elif Question_2 =='no':
##               counter =   counter +1
##               Question_3= raw_input('Is the number greater than 15, please enter yes or no: ')
##               if Question_3 =='yes':
##                  counter = counter +1
##                  Question_4= raw_input('Is the number 17, please enter yes or no: ')
##                  if Question_4 == 'yes':
##                      print 'Mystic Forces have correctly predicted the number to be 17 and the guess count is ' + str(counter)
##                      break
##                  else:
##                      print 'Mystic Forces have correctly predicted the number to be 19 and the guess count is ' + str(counter)
##                      break
##               elif Question_3 =='no':
##                   counter = counter +1
##                   Question_4= raw_input('Is the number 15, please enter yes or no: ')
##                   if Question_4 == 'yes':
##                      print 'Mystic Forces have correctly predicted the number to be 15 and the guess count is ' + str(counter)
##                      break
##                   else:
##                      print 'Mystic Forces have correctly predicted the number to be either 11 or 13 and the guess count is ' + str(counter)
##
##
##    elif Question_1 =='no':
##           counter = counter +1
##           Question_2= (raw_input('Is the number even, please enter yes or no: '))
##           if Question_2 =='yes':
##              counter =   counter +1
##              Question_3= raw_input('Is the number greater than 6, please enter yes or no: ')
##              if Question_3 =='yes':
##                  counter = counter +1
##                  Question_4= raw_input('Is the number 8, please enter yes or no: ')
##                  if Question_4 == 'yes':
##                      print 'Mystic Forces have correctly predicted the number to be 8 and the guess count is ' + str(counter)
##                      break
##                  else:
##                      print 'Mystic Forces have correctly predicted the number to be 10 and the guess count is ' + str(counter)
##                      break
##
##              elif Question_3 =='no':
##                      counter = counter +1
##                      Question_4= raw_input('Is the number 6, please enter yes or no: ')
##                      if Question_4 == 'yes':
##                         print 'Mystic Forces have correctly predicted the number to be 6 and the guess count is ' + str(counter)
##                         break
##                      else:
##                          print 'Mystic Forces have correctly predicted the number to be either 2 or 4 and the guess count is ' + str(counter)
##                          break       
##
##
##           elif Question_2 =='no':
##                 counter =   counter +1
##                 Question_3= raw_input('Is the number greater than 5, please enter yes or no: ')
##                 if Question_3 =='yes':
##                    counter = counter +1
##                    Question_4= raw_input('Is the number 7, please enter yes or no: ')
##                    if Question_4 == 'yes':
##                      print 'Mystic Forces have correctly predicted the number to be 7 and the guess count is ' + str(counter)
##                      break
##                    else:
##                      print 'Mystic Forces have correctly predicted the number to be 9 and the guess count is ' + str(counter)
##                      break
##
##                 elif Question_3 =='no':
##                      counter = counter +1
##                      Question_4= raw_input('Is the number 5, please enter yes or no: ')
##                      if Question_4 == 'yes':
##                       print 'Mystic Forces have correctly predicted the number to be 5 and the guess count is ' + str(counter)
##                       break
##                      elif Question_4 == 'no':
##                       print 'Mystic Forces have correctly predicted the number to be either 1 or 3 and the guess count is ' + str(counter)
##                       break
##
##
##    else:
##        print ' The guess counter has reached the count ' + str(counter)
##else:
##        print 'Please check the number you have entered, you can enter a number from 1 to 20 only '
##
##
####**** write a program for a palindrome
##
####word= raw_input('Please enter the word that you want to check for the condition of palindrome: ')
####flipped= word [::-1]
####if word == flipped:
####   print ' The entered word is a palindrome because you entered '+ str(word) + ' , and the reversed word is also ' + str(flipped)
####else:
####   print 'The word is not a palindrome' + ' you entered ' + str(word) + ' , but the reversed word is ' + str(flipped)
