import math

number = int(input())
kg_count = 0

for i in range(math.ceil(number / 5), -1, -1):
    plastic_bag = number - (5 * i)

    if 0 < plastic_bag < 3 or plastic_bag < 0:
        continue

    elif plastic_bag == 0:
        kg_count += i
        break

    else:
        check = plastic_bag % 3

        if not check:
            kg_count += (i + int(plastic_bag / 3))
            break

        else:
            continue

if kg_count == 0:
    kg_count -= 1

print(kg_count)