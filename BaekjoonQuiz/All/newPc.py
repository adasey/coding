import sys

typed = int(sys.stdin.readline())

for a in range(typed):
    case, data = sys.stdin.readline().split()

    case, data = int(case), int(data)

    end = str(case ** (data % 4 if data % 4 else 4))

    if end[-1] != "0":
        print(end[-1])

    else:
        print("10")