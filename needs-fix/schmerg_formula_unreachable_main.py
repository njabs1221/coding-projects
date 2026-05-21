

import math

def schmerg(x, y):
    numerator = (x * y+ math.sin(x) * math.cos(x) * math.tan(x) + (x + 654314) / y)  
    denominator = (x**2 * y**(-3) + math.log(y + 12))
    return numerator / denominator

    x = float(input())
    ans1=schmerg((0.5*x),(0.7*x))
    ans2=schmerg(x, ans1)
    ans3=schmerg((x+1), (x-1))
    ans4=schmerg(ans2, ans3)
    print(ans4)