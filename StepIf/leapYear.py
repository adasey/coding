import sys

number = int(sys.stdin.readline().rstrip())
num = 0

if number % 4 == 0:
    if number %  100 == 0:
        num = 1 if number % 400 == 0 else 0

    else:
        num = 1

print(num)