typed = [list(a) for a in input().split()]

typed[0].reverse()
typed[1].reverse()

first, second = ["".join(a) for a in typed]
print(first if first > second else second)