y=int(input())
if y%100==0 and y%400==0:
    print(y, "is a leap year")
elif y%100!=0 and y%4==0:
    print(y, "is a leap year")
else:
    print(y, "is not a leap year")
    
