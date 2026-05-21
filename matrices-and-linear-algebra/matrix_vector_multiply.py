def matrix_vector_multiply(matrix, vector):
    result = []
    for row in matrix:
        total = 0
        for i in range(len(vector)):
            total += row[i] * vector[i]
        result.append(total)
    return result


rows, cols = map(int, input().split())
matrix = []

for _ in range(rows):
    row = [float(value) for value in input().split()]
    matrix.append(row)

vector = [float(value) for value in input().split()]

if len(vector) != cols:
    print("Vector length does not match matrix columns")
else:
    output = matrix_vector_multiply(matrix, vector)
    print(" ".join(str(value) for value in output))
