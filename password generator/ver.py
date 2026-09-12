
num3=input("enter password-->")
lowerCase=0
upperCase=0
digit=0
special_char=0;;;
for character in num3:
  if(character.isupper()):
    upperCase=1
  if(character.islower()):
      lowerCase=1
  if(character.isdigit()):
     digit=1
  if(not character.isalnum()):
     special_char=1
if(lowerCase==1 and upperCase==1 and digit==1 and len(num3)>=8 and special_char==1):
   print("✅strong password")
else:
   print("❌ password")
   print("mising is")
   if(upperCase==0 ):
    print(" ❌add an upperCase letter:")
   if(lowerCase==0 ):
    print("❌add an lowercase letter:")
   if(len(num3)<8 ):
    print("❌add an length:")
   if(special_char==0):
    print("❌add an alphanum number")
   if(digit==0):
    print("❌add an digit:")


