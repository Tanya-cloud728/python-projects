numbers=int(input("Enter number-->"))
list=[]
accumulator=0

for i in range(numbers):
    n=int(input(f"enter number{i+1}-->"))
    list.append(n)
    
print(list)
for i in range(numbers):
    accumulator=accumulator+list[i]
    average=accumulator/numbers
print("sum of numbers are::",accumulator)
print("average is::",average)
print("maximum number is::",max(list))
print("minimum number is::",min(list))
range1=max(list)-min(list)
print("range is::",range1)
even_cnt=0
odd_cnt=0
positive_cnt=0
negative_cnt=0
zero_cnt=0
for i in range(numbers):
    if(list[i]>0):
        positive_cnt+=1
    elif(list[i]==0):
        zero_cnt+=1
    else:
        negative_cnt+=1
for i in range(numbers):
    if(list[i]%2==0):
        even_cnt+=1
    else:
        odd_cnt+=1
print("even numbers are->",even_cnt)
print("odd numbers are->",odd_cnt)
print("number of 0 are::",zero_cnt)
print("number of positive numbers are::",positive_cnt)
print("number of negative numbers numbers are::",negative_cnt)
list.sort()
print(list)
if(numbers%2!=0):
    print("Median is",list[numbers//2])
else:
    x=(list[numbers//2]+list[numbers//2-1])/2
    print("median is::",x)
list.reverse()
print(list)
length=len(list)
print(length)
        
