import sys

# hour, minute = map(int, sys.stdin.readline().split()) 를 사용해 본 결과 시간에서 더 오래걸림. 적은 양의 데이터는  별로이거나 시간의 효율이 안좋은듯 하다.
hours = [int(a) for a in sys.stdin.readline().split()]
hour, minute = hours[0], hours[1]

minute -= 45
if minute < 0:
    hour -= 1
    minute = 60 + minute

hour = 23 if hour < 0 else hour

print(f"{hour} {minute}")