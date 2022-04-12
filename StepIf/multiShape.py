import sys

number = int(sys.stdin.readline())
if number > 0:
    print(1) if int(sys.stdin.readline()) > 0 else print(4)

else:
    print(2) if int(sys.stdin.readline()) > 0 else print(3)