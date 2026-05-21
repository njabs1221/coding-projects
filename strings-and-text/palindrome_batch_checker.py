

#Question 4

num=int(input())
count=0
while count<num:
    word=(input())
    if word[::-1]==word:
        print("True")
    else:
        print("False")
    count+=1