import sys
import math as m

input = sys.stdin.readline

for _ in range(int(input())):
    height, width, n_customer = map(int, input().split())

    room = m.ceil(n_customer / height)
    floor = n_customer % height if n_customer % height else height

    print(f"{floor}{str(room).zfill(2)}")