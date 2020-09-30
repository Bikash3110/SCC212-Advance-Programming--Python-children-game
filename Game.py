import math
import random

"""This class asks questions and check answer on addtion, subtrcation, multiplication
   and division operations and a random option focused on teaching young children arithmatic."""
class SimpleArithmatic:

 """Addition Funtion ask questions depending on range(i.e level) and return
    1 or 0 representing correct or wrong respectively depending on the answer of the user.
    @param List is the list of integers """   
 def addition(List):
  try:                                            # try -> to catch exception 
   integer1 = random.choice(List)   
   integer2 = random.choice(List)
   print("What is ",integer1,"+",integer2," ?")
   sum = integer1 + integer2
   answer = input()                                # Takes user Input
   if int(answer) == sum:                         # compares user input from the actual addition output  
     print("That is correct, well done!\n")
     count = 1                                     #returns 1 if user input is correct else 0
   else:
     count = 0   
     print("Not right,the correct answer is ",sum,"\n") 
   return count
  except (Exception):                              # If Exception caught in try then this block is executed 
    print("ERROR: Enter Answer in Interger ")  

 """Subtraction Funtion ask questions depending on range(i.e level) and return
    1 or 0 representing correct or wrong respectively depending on the answer of the user.
    Keeping requirements in mind, this funtion doen't ask a question which has negative output
    @param List is the list of integers """
 def subtraction(List):
  try:   
   integer1 = random.choice(List)   
   integer2 = random.randint(1,integer1)
   print("What is ",integer1,"-",integer2," ?")   # Question displayed related to arithmatic operator  
   diff = integer1-integer2                       # compares user input from the actual subtraction output
   answer = input()
   if int(answer) == diff:
    count= 1   
    print("That is correct, well done!\n")
   else:
    print("Not right,the correct answer is ",diff,"\n")
    count= 0
   return count 
  except(Exception):  
    print("ERROR: Enter Answer in Interger ")

 """Multiplication Funtion ask questions depending on range(i.e level) and return
    1 or 0 representing correct or wrong respectively depending on the answer of the user.
    @param List is the list of integers """
 def multiplication(List):
  try:   
   integer1 = random.choice(List)
   integer2 = random.choice(List)
   print("What is ",integer1,"*",integer2," ?")
   product = integer1*integer2
   answer = input()
   if int(answer) == product:                    # compares user input from the actual multiplication output 
    count= 1
    print("That is correct, well done!\n")
   else:   
    print("Not right,the correct answer is ",product,"\n")
    count= 0
   return count 
  except(Exception):
    print("ERROR: Enter Answer in Interger ")
    
 """Division Funtion ask questions depending on range(i.e level) and return
    1 or 0 representing correct or wrong respectively depending on the answer of the user.
    Funtion does not have fractional value.
    @param List is the list of integers """
 def division(List):
  try:   
   integer1 = random.choice(List)
   sublist = []
   for i in range(1,integer1+1):                #factor of interger1 to avoid fractional results.
     if integer1%i==0:                          #for loop checks the factors of integer1 and store the  
      sublist.append(i)                         #values in the sublist for integer2 random choice. 
   integer2 = random.choice(sublist)
   print("What is ",integer1,"/",integer2," ?")
   div = integer1/integer2
   answer = input()
   if int(answer) == div:
    count= 1
    print("That is correct, well done!\n")
   else:  
    print("Not right,the correct answer is ",div,"\n")
    count= 0
   return count
  except(Exception):
    print("ERROR: Enter Answer in Interger ")

 #Prompts user with a yes_no question and returns response	   
 def askYesNo(question):
  try:   
   response = None
   while response not in ('y','n'):              # loop iterates unless the response is 'Y' or 'N'
    response = input(question).lower()
   return response 
  except(Exception):
    print("ERROR: Enter Answer in Interger ")
    
 """Increase or Decrease game level when user gives 3 consecutive
    right or wrong answers respectively.
    @param correct, @param wrong contain number of correct and wrong answers.
    @param level pass current level value and the funtion returns the updated value"""
 def checkLevel(correct,wrong,level):
  try: 
   if correct==3 and level<7:                    # Checks number of consecutive correct answers and if level<7 
      level+=1                                   # Level up if requirements met 
      print('Wow! Level Up ---- LEVEL ',level,'-----')  
   elif wrong == -3 and level>1:                 # Checks number of consecutive wrong answers and if level>1 
      level-=1                                   # Level down if reqirement met
      print('Oops! Level Down ---- LEVEL ',level,'-----')
   return level                                  # returns updated level  
  except(Exception):
    print("ERROR: Enter Answer in Interger ")
      
#-----------Main program---------------
 list = [[1,2,3,4],[1,2,3,4,5],[1,2,3,4,5,6],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9,10]]
 
 #----All arithmatic operations start with LEVEL 1 questions by default---------
 select = None 
 while select != "6":
  try:   
   print("\nSelect option below \n")
   print('1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Random 6.Quit')
   select = input()                              #prompts for choice
	
   if select =='1':                              #Selects Addition related arithmetic questions and checks answers
     z = None
     correct=wrong=0                             # Initialize correct and wrong to ZERO to clear all previous values
     level=1
     while z != 'n':
       if addition(list[level-1])== 1:           # Check if user input is correct ot not  
         correct+= 1                             # increament Correct
         wrong= 0                                # set wrong to zero  
       else:
         correct= 0
         wrong-= 1                               # decreament wrong 
       if correct == 3 or wrong ==-3:            # checks if user input consecutivly correct or wrong 3times  
        level = checkLevel(correct,wrong,level)  # calls the Checklevel() and update the level 
        wrong = correct =0                       # reset wrong and correct values  
       z = askYesNo("Press 'Y' to try another sum or 'N' to stop\n")           

   if select == '2':                            #Selects subtraction related arithmetic questions and checks answers
     z = None
     correct=wrong=0
     level=1
     while z != 'n':
       if subtraction(list[level-1])== 1:
         correct+= 1
         wrong= 0
       else:
         correct= 0
         wrong-= 1 
       if correct == 3 or wrong ==-3: 
        level = checkLevel(correct,wrong,level)
        wrong = correct =0
       z = askYesNo("Press 'Y' to try another sum or 'N' to stop\n")

   if select == '3':                            #Selects multiplication related arithmetic questions and checks answers
     z = None
     correct=wrong=0
     level=1
     while z != 'n':
       if multiplication(list[level-1])== 1:
         correct+= 1
         wrong= 0
       else:
         correct= 0
         wrong-= 1 
       if correct == 3 or wrong ==-3: 
        level = checkLevel(correct,wrong,level)
        wrong = correct =0    
       z = askYesNo("Press 'Y' to try another sum or 'N' to stop\n")

   if select == '4':                            #Selects division related arithmetic questions and checks answers
     z = None
     correct=wrong=0
     level=1
     while z != 'n':
       if division(list[level-1])== 1:
         correct+= 1
         wrong= 0
       else:
         correct= 0
         wrong-= 1 
       if correct == 3 or wrong ==-3: 
        level = checkLevel(correct,wrong,level)
        wrong = correct =0  
       z = askYesNo("Press 'Y' to try another sum or 'N' to stop\n")

   if select == '5':                           #Selects random arithmetic questions(add,sub,mul,div) and checks answers
     z = None
     correct=wrong=0
     level=1
     while z != 'n':
       operator = random.choice(['+','-','*','/'])      #Selects random arithmetic operator from the given list
       if(operator == '+'):                     # '+' operator from random select     
          if addition(list[level-1])== 1:
            correct+= 1
            wrong= 0
          else:
            correct= 0
            wrong-= 1    
       elif(operator == '-'):                   # '-' operator from random select
          if subtraction(list[level-1])== 1:
            correct+= 1
            wrong= 0
          else:
            correct= 0
            wrong-= 1   
       elif(operator == '*'):                    # '*' operator from random select
          if multiplication(list[level-1])== 1:
            correct+= 1
            wrong= 0
          else:
            correct= 0
            wrong-= 1      
       elif(operator == '/'):                    # '/' operator from random select
          if division(list[level-1])== 1:
            correct+= 1
            wrong= 0
          else:
            correct= 0
            wrong-= 1
       if correct == 3 or wrong ==-3: 
        level = checkLevel(correct,wrong,level)
        wrong = correct =0   
       z = askYesNo("Press 'Y' to try another sum or 'N' to stop\n")
  except(Exception):
   print("ERROR: Enter Answer in Interger ")
