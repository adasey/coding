number = int(input())

NATURE = [a for a in range(10)]

def unberHun(number):
    count = 0
    result = 0
    for a in range(10, number + 1):
        for b in str(a):
            if result == int(b):
                continue

            else:
                result = int(b)
        
        count += 1

    return count

print(unberHun(number))