croatia = {'c' : {"=": 1, "-": 1}, 'd': {"z=": 2, "-": 1}, 'l': {"j": 1}, 'n': {'j': 1}, 's': {"=": 1}, 'z': {"=": 1}}
alpha_count = 0
i = 0

typed = input()

while True:
    if typed[i] in croatia:
        try:
            if typed[i+1] in croatia[typed[i]]:
                alpha_count += 1
                i += 1

            elif (typed[i+1] + typed[i+2]) in croatia[typed[i]]:
                alpha_count += 1
                i += 2

            else:
                alpha_count += 1

        except:
            alpha_count += 1    

    else:
        alpha_count += 1

    i += 1

    if i >= len(typed):
        break

print(alpha_count)