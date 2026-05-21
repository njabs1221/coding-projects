#Question 2

s=input()
count=0
index=0
while index<len(s):
    c=s[index]
    if 'A'<=c<='Z':
        count+=1
    index+=1
print(count)