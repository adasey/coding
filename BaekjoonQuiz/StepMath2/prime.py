from math import sqrt

prime = []
low_value, high_value = int(input()), int(input())

def findPrime(number, check):
    if check > 1:
        if number % check == 0:
            return False
        
        else:
            return findPrime(number, check - 1)
    
    else:
        return True

for i in range(low_value, high_value + 1):
    if i <= 2:
        if i == 1:
            continue
        
        prime.append(i)

    else:
        if findPrime(i, int(sqrt(i))):
            prime.append(i)

try:
    prime[0]
    print(sum(prime))
    print(prime[0])

except:
    print(-1)