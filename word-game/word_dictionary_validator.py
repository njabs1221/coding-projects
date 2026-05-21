n=input()
words=[]

o=len(n)
c=0
while n!="###" and o==5:
    k=n.upper()
    n=input()
    words.append(k)
    c+=1
p=input()
j=p.upper()

if j in words:
    print("Valid")
else:
    print("Invalid")
    