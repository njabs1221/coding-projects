n=int(input())
y=input()
x=int(input())
p=1
d={y:x}
while p<n:
    y=input()
    x=int(input())
    d[y]=x
    p+=1
print(d, sep='\n')