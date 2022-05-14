import math as m

index = int(input())

pos_x = int(-0.5 + m.sqrt(0.25 + (2 * index)))
base = int((pos_x * (pos_x + 1)) / 2)
pos_y = index - base

if not (pos_x % 2):
    if base == index:
        print(f"{pos_x}/{pos_y + 1}")

    else:
        pos_x += 1
        print(f"{pos_x + 1 - pos_y}/{pos_y}")

else:
    if base == index:
        print(f"{pos_y + 1}/{pos_x}")

    else:
        pos_x += 1
        print(f"{pos_y}/{pos_x + 1 - pos_y}")