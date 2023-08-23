
string=input("Enter a string")
vowels=['a','e','i','o','u','A','E','I','O','U']
cnt=0 #
index=0
length=len(vowels)
while index < length:
    cnt=cnt+string.count(vowels[index])
    index=index+1

print("Count is",cnt)
