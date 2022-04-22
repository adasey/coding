def solution(participant, completion):
    answer = ''
    dic = {}
    temp = 0
    
    for a in participant:
        dic[hash(a)] = a
        temp += hash( a)
        
    for b in completion:
        temp -= hash(b)
        
    answer = dic[temp]
    
    return answer