word = input().lower()

dic = {}
a = 1
c = 0
result = ""

for i in word:
    try:
        dic[i] += 1
    except:
        dic[i] = a

for a, b in dic.items():
    if b == max(dic.values()):
        result = str(a).upper()
        c += 1

    if c > 1:
        result = "?"
        break

print(result)