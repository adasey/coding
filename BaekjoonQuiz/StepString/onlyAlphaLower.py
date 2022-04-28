import string

alpha_lower = {a: -1 for a in string.ascii_lowercase}

typed = input()

for a, b in enumerate(typed):
    if b in alpha_lower:
        if alpha_lower[b] <= -1:
            alpha_lower[b] = a

for a in alpha_lower.values():
    print(a, end=" ")