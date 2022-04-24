total = int(input())

test_scores = [int(a) for a in input().split()]

edit_scores = [(a / max(test_scores)) * 100 for a in test_scores]

average = sum(edit_scores) / total

print(average)