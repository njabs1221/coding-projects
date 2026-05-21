import math
import sys
def matrix_1_norm(v, r):
    total = 0
    for value in range(r):
        r_sum=0
        for row in v:
            r_sum=r_sum+abs(row[value])
            if r_sum>total:
                total=r_sum
    return total

def frob_2_norm(v):
    total = 0
    for row in v:
        for value in row:
            total += value ** 2
    return math.sqrt(total)

def matrix_inf_norm(v):
    total = 0
    for row in v:
        row_total=0
        for value in row:
            row_total=row_total+abs(value)
            if row_total>total:
                total=row_total 
    return total

def main():
    c, r=map(int, input().split())
    v=[]
    for i in range(c):
        row=[float(x) for x in input().split()]
        v.append(row)
        
    print(f"{matrix_1_norm(v, r):.6f}")
    print(f"{matrix_inf_norm(v):.6f}")
    print(f"{frob_2_norm(v):.6f}")
if __name__ == "__main__":
    main()