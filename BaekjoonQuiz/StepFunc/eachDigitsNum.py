number = int(input())

def showHanNum(number):
    count = 99

    if underHundred(number):
        print(number)
    
    else:
        if number > 110:
            if number > 999:
                number = 999
            
            number += 1

            for num in range(111, number):
                check = [str(num)]
                
                first, second = int(check[0][0]) - int(check[0][1]), int(check[0][1]) - int(check[0][2])

                if first == second:
                    count += 1

            print(count)
        
        else:
            print(count)

def underHundred(number):
    return True if number < 100 else False

showHanNum(number)