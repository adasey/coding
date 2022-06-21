import math
number = int(input())
result = []

if number > 1:
    for i in range(2, number):
        
        while number % i == 0:
            number = int(number / i)
            result.append(i)

    if len(result) > 1:
        for a in result:
            print(a)

    else:
        print(number)