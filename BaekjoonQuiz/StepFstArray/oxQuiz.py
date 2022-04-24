import sys

result = 0

def sigmaO(number):
    return int(((number) * (number + 1)) / 2)

for _ in range(int(sys.stdin.readline())):
    answered = sys.stdin.readline().split("X")

    for a in answered:
        if len(a):
            result += sigmaO(a.count("O"))

    print(result)
    result = 0