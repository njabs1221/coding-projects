x=int(input())
y=[]
for i in range(x):
    num= int(input())
    y.append(num)
y.sort()
if len(y)%2!=0:
    med=y[len(y)//2]
    print(med)
else:
    med1=y[len(y)//2-1]
    med2=y[len(y)//2]
    print((med1+med2)/2)