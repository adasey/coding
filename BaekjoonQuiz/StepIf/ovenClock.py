import sys

hours = [int(a) for a in sys.stdin.readline().split()]
hour, minute = hours[0], hours[1]

minute += int(sys.stdin.readline().strip())

while minute >= 60:
    minute -= 60
    hour += 1

hour = hour - 24 if hour >= 24 else hour
print(f"{hour} {minute}")