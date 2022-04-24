import sys

for _ in range(int(sys.stdin.readline())):
    test_case = [int(a) for a in sys.stdin.readline().split()]

    count = 0
    total = test_case.pop(0)
    average = sum(test_case) / total

    for a in test_case:
        if a > average:
            count += 1

    over_average = (count / total) * 100

    print(f"{format(round(over_average, 3), '.3f')}%")