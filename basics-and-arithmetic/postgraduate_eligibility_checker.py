average_mark=float(input())
work_experience=int(input())
honours_degree=str(input())
if average_mark>=65: 
    if work_experience>=2 or honours_degree=="yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
    


