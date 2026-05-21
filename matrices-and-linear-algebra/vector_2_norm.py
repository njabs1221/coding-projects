import math
import sys
def vector_2_norm(v):
    total = 0
    for value in v:
        total += value ** 2
    return math.sqrt(total)
def main():
    data = sys.stdin.read().strip().splitlines()
    n = int(data[0])
    v = [float(x) for x in data[1].split()]
    if len(v) != n:
        raise ValueError("Vector length does not match n")
    print(f"{vector_2_norm(v):.6f}")
if __name__ == "__main__":
    main()