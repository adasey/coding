import sys

score = ["A", "B", "C", "D", "F"]

number = int(sys.stdin.readline().rstrip())

if number >= 90:
    print(score[0])

elif number >= 80 and number < 90:
    print(score[1])

elif number >= 70 and number < 80:
    print(score[2])

elif number >= 60 and number < 70:
    print(score[3])

else:
    print(score[4])