import math

def primeNumber(factor, number):
    if factor > 1:
        if number % factor:
            return primeNumber(factor - 1, number)
        else:
            return False
    else:
        return True

def checkPrime():
    input()
    count = 0
    for i in map(int, input().split()):
        if i != 1:
            if primeNumber(int(math.sqrt(i)), i):
                count += 1

    return count

print(checkPrime())
