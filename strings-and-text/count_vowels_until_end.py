word=input()
plo=["a","e","i","o","u"]
while word!="end":
    vowel=0
    line=word.lower()
    for chr in line:
        if chr in plo:
            vowel+=1
    print(vowel)
    word=input()
    
