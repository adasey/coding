import sys

typed = int(sys.stdin.readline())
i = 0

while True:
    if typed == i:
        break

    numbers = [int(a) for a in sys.stdin.readline().split()]
    print(numbers[0] + numbers[1])

    i += 1
