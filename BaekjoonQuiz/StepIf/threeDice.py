import sys

numbers = [int(a) for a in sys.stdin.readline().split()]
fst, snd, trd = numbers

if fst == snd == trd:
    print(10000 + fst * 1000)

elif fst == snd != trd:
    print(1000 + fst * 100)

elif snd == trd != fst:
    print(1000 + snd * 100)

elif fst == trd != snd:
    print(1000 + trd * 100)

else:
    print(max(numbers) * 100)