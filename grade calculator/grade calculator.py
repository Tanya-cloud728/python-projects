totalMarks=int(input("total marks is:"))
if(totalMarks>100) :
 obtmarks=int(input("enter your marks:"))
 if(obtmarks<totalMarks):
  percentage=(obtmarks/totalMarks)*100
  print(percentage)
 if(90<=percentage<=100):
    print("A")
    print("Excellent!")
 elif(80<=percentage<=89):
    print("B")
    print("very good!")
 elif(70<=percentage<=79):
    print("C")
    print("good!")
 elif(60<=percentage<=69):
    print("D")
    print("needs to improve!")
 else:
    print("F")
    print("bad")
else:
   print("invalid marks:")