import sys

typed = int(sys.stdin.readline())

for a in range(typed):
    case, data = sys.stdin.readline().split()
    case, data = int(case), int(data[-1])

    print(data)
    if str(case ** data)[-1] == "0":
        print("10")

    else:
        print(str(case ** data)[-1])