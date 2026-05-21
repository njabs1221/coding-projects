def is_prime(x):
    if x<=1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True



def is_twin_prime(x):	
    if is_prime(x) and (is_prime(x-2) or is_prime(x+2)):
        return True
    else:
        return False
	


N = int(input())
for i in range(N):
    p = int(input())
    if is_twin_prime(p):
        print("true")
    else:
        print("false")

