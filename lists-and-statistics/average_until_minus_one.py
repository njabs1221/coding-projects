total=0
count=0
x=float(input())
while x!=-1:
    total+=x
    count+=1
    x=float(input())
if count>0:
    print(total/count)
