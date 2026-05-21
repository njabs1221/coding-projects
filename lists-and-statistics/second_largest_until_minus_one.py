numbers = []

while True:
    num = int(input())
    if num == -1:
        break
    numbers.append(num)

numbers.sort(reverse=True)
print(numbers[1])