x=input()
y=[]
while x!="###":
    y.append(x)
    x=input()
y.reverse()
for i in y:
    print(i, sep='\n')