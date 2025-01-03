#count the vowels in a string 
word=input("Enter a single word :")
vowels='a,e,i,o,u'
count=0
for n in word.lower():
    if n in vowels:
        count=count+1
print("Number of vowels in this word : {}".format(count))   