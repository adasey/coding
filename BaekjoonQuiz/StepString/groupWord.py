import sys

typed = sys.stdin.readline

time = int(typed())

is_group = True
count = 0

for _ in range(time):
    word = typed()

    word_check = {}

    for x, y in enumerate(word):
        if y in word_check:
            if (word_check[y] + 1) != x:
                is_group = False

            else:
                word_check[y] = x

        else:
            word_check[y] = x

    if is_group:
        count += 1

    is_group = True

print(count)