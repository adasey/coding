import sys

sys.stdin.readline()
numbers = [int(a) for a in sys.stdin.readline().split()]

print(f"{min(numbers)} {max(numbers)}")