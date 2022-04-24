import sys

DIV_NUM = 42
result = {}
count = 0

def isNone(check):
    if check is None:
        return False

    else:
        return True

for _ in range(10):
    number = int(sys.stdin.readline())
    div = number % DIV_NUM

    if isNone(result.get(div)):
        continue

    else:
        result[div] = 0
        count += 1

print(count)
