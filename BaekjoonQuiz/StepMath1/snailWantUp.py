import math as m

day, night, height = map(int, input().split())

print(m.ceil((height - day) / (day - night)) + 1)