f = input().upper()
s = input().upper()

r = []
fc = [False] * 5
sc = [False] * 5


for i in range(5):
    if f[i] == s[i]:
        r.append(s[i])
        fc[i] = True
        sc[i] = True
    else:
        r.append(None)


for i in range(5):
    if r[i] is None:
        found = False
        for j in range(5):
            if not fc[j] and s[i] == f[j]:
                r[i] = f[j].lower()
                fc[j] = True
                found = True
                break
            if found == True:
    else:
        if not fc[j] and s[i] == f[j]:
            r[i] = s[i].lower()
            fc[j] = True
            break            
        if not found:
            r[i] = '.'

print(''.join(r))