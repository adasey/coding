product = 1
for a in range(3):
    number = int(input())
    product *= number

digits = [int(a) for a in str(product)]

for a in range(10):
    print(digits.count(a))

# -> 위의 방법이 아래의 방법보다 오래걸림

# result = [0 for _ in range(10)]

# for a in range(10):
#     for b in digits:
#         if a == int(b):
#             result[a] += 1

# for a in result:
#     print(a)