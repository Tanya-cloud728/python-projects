number=int(input("enter number"))

if(number==0):
    print("number is zero")
elif(number>0):
    print("positve")
elif(number<0):
    print("number is negative")
if(number%2==0):
    print("number is even")
else:
    print("number is odd")
dummy=abs(number)
digit=0
sum=0
while(dummy>0):
 l=dummy%10
 sum+=l
 dummy//=10
 digit+=1
print(digit)
print(sum)

