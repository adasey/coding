import sys

numbers = [int(a) for a in sys.stdin.readline().split()]

if numbers[0] > numbers[1]:
    print(">")

elif numbers[0] < numbers[1]:
    print("<")

else:
    print("==")