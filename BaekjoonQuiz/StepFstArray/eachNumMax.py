import sys

numbers = []
for a in range(9):
    numbers.append(int(sys.stdin.readline()))

print(max(numbers))
print(numbers.index(max(numbers)) + 1)