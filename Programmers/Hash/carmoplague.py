def solution(clothes):
    clothe_kind = {}
    each_length = []
    
    for a in clothes:
        if a[1] in clothe_kind:
            clothe_kind[a[1]].append(a[0])
            
        else:
            clothe_kind[a[1]] = [a[0]]
            
    for a in clothe_kind.values():
        each_length.append(len(a))
        
    return calChance(len(clothe_kind), each_length, 0)
            
def calChance(chance, cal, result):
    if chance == 0:
        return result
    
    if chance == 1:
        return calChance(chance - 1, cal, sum(cal) + result)
    
    if chance == 2:
        for a in range(len(cal)):
            if a + 1 <= len(cal):
                for b in cal[a + 1:]:
                    result += (cal[a] * b)
        
        return calChance(chance - 1, cal, result)
    
    if chance == 3:
        for a in range(len(cal)):
            if a + 2 <= len(cal):
                for b in range(a + 1,len(cal)):
                    for c in cal[b + 1:]:
                        result += (cal[a] * cal[b] * c)
                        
        return calChance(chance - 1, cal, result)
    
    if chance == 4:
        return calChance(chance - 1, cal, cal[0] * cal[1] * cal[2] * cal[3])
    