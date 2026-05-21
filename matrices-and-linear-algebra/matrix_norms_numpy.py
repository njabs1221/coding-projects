import numpy as np

def matrix_norm_1_numpy(A):
    return np.linalg.norm(A, 1)

def matrix_norm_inf_numpy(A):
    return np.linalg.norm(A, np.inf)

def frob_norm_numpy(A):
    return np.linalg.norm(A, 'fro')

def main():
    rows, cols = map(int, input().split())
    matrix = []
    for _ in range(rows):
        row = [float(x) for x in input().split()]
        matrix.append(row)

    A = np.array(matrix, dtype=float)

    print(f"{matrix_norm_1_numpy(A):.6f}")
    print(f"{matrix_norm_inf_numpy(A):.6f}")
    print(f"{frob_norm_numpy(A):.6f}")

if __name__ == "__main__":
    main()
