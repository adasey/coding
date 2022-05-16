import sys
input = sys.stdin.readline

for _ in range(int(input())):
    floor = int(input())
    room = int(input())

    residence_count = [a for a in range(1, room + 1)]

    if floor > 1:
        for i in range(1, floor):
            temp = []

            for j in range(1, room + 1):
                temp.append(sum(residence_count[0:j]))

            residence_count = temp

    print(sum(residence_count[0:room + 1]))