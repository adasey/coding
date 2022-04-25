def selfNumberCalculate():
    number = 10000

    creatorNum = []
    selfNum = [i for i in range(1, number + 1)]

    for a in selfNum:
        if a < 10:
            creatorNum.append(a + a)

        elif 10 <= a < 10**2:
            creatorNum.append(a + (a % 10) + int(a / 10))

        elif 10**2 <= a < 10**3:
            creatorNum.append(a + (a % 10) + int(a / 10**2) + int((a % 10**2) / 10))

        elif 10**3 <= a < 10**4:
            creatorNum.append(a + (a % 10) + int(a / 10**3) + int((a % 10**3) / 10**2) + int(((a % 10**3) % 10**2) / 10))

    creatorNum.sort()
    for a in creatorNum:
        try:
            selfNum.remove(a)
        except:
            continue
    
    for a in selfNum:
        print(a)
        
selfNumberCalculate()