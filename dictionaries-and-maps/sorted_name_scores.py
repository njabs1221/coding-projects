n=int(input())
d={}
for i in range(n):
    y=input()
    x=int(input())
    d[y] = x
o=sorted(d.items())
u="\n".join([f"{y} : {x}"for y, x in o])
print(u)