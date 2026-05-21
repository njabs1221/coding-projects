f = input().upper()
s = input().upper()

r = ["."]*5
fc = [False] * 5


for i in range(len(f)):
    if f[i] == s[i]:
        r[i]=s[i]
        fc[i] = True



for i in range(len(f)):
    if r[i] != '.':
        continue
    for j in range(len(f)):
        if not fc[j] and s[i] == f[j]:
            r[i] = s[i].lower()
            fc[j] = True
            break
        

print(''.join(r))