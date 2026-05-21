def matrix_vector_multiply_manual(A, x):
    result = []
    for row in A:
        total = 0
        for j in range(len(x)):
            total = total + row[j] * x[j]
        result.append(total)
    return result

def main():
    A=map(int, input().split())
    A=[]
    for i in range(A):
        row=[float(x) for x in input().split()]
        A.append(row)

def main():
    x=map(int, input().split())
    x=[]
    for i in range(x):
        row=[float(x) for x in input().split()]
        x.append(row)

print(matrix_vector_multiply_manual(A, x))
