sentence=input("Enter your sentence->")
print(len(sentence))
print(len(sentence.split()))
sentence=sentence.lower()
vowel=0
digit=0
for i in range (len(sentence)):
 if(sentence[i]=='a'or sentence[i]=='e' or sentence[i]=='i' or sentence[i]=='o' or sentence[i]=='u'):
  vowel+=1
 if(sentence[i].isdigit()):
  digit+=1
print(vowel)
print(digit)