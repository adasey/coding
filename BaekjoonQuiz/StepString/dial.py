starts = [ord('A'), ord('D'), ord('G'), ord('J'), ord('M'), ord('P'), ord('T'), ord('W')]
total = 0

typed = input()

for a in typed:
    text = ord(a)

    for x, y in enumerate(starts):
        if text >= y:
            number = x + 3

        else:
            break

    total += number

print(total)