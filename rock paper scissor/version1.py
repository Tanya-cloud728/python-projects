# import random                               #random is a module and import choose from random module
# count=0
# score=0
# compScore=0
# choices=["rock","paper","scissor"]
# while(count<5):
#  comp=random.choice(choices)
#  print("enter choice")
#  uc=input("enter your choice:")
#  uc=uc.lower()
#  print(comp)
#  if(uc=="rock" or uc=="paper" or uc=="scissor"):                
#   if(uc==comp):                                                     #this will run until whilw loop false
#     print("draw")
#   elif( uc=="Rock" and comp=="scissor"):
#     print("you wins")
#     score+=score
#   elif( uc=="Paper" and comp=="rock"):
#     print("you win")
#     score+=score
#   elif( uc=="Scissor" and comp=="paper"):
#     print("you win")
#     score+=1
#   else:
#     print("computer wins")
#     compScore+=1
#   count+=1
#  else:
#   print("invalid input")
#   count=count+1
# print("game over")
# print("your score is:",score)  
# print("comp score is:",compScore)
# if(score == compScore):
#   print("equal score")
# elif(score<compScore):
#   print("comp win")
# else:
#   print("we won")



import random
nums=input("entetr word:")
print(len(nums))