import sys

typed = int(sys.stdin.readline())

for _ in range(typed):
    result = ""
    repeat, text = sys.stdin.readline().split()

    for a in text:
        result += a * int(repeat)

    print(result)