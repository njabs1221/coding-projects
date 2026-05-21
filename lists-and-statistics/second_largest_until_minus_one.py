numbers = []

while True:
    value = int(input())
    if value == -1:
        break
    numbers.append(value)

if len(numbers) < 2:
    print("Not enough numbers")
else:
    numbers.sort()
    print(numbers[-2])
