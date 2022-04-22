def solution(clothes):
    clothe_kind = {}
    result = 1
    
    for a in clothes:
        if a[1] in clothe_kind:
            clothe_kind[a[1]].append(a[0])
            
        else:
            clothe_kind[a[1]] = [a[0]]
            
    for a in clothe_kind.values():
        result *= (len(a) + 1)
        
    return result - 1

    # 확률 계산에 대한 오류
    # 각 예시별 의류의 입고 벗고에서 의상의 최대 개수에 벗는 다는 1의 가정과 마지막에 전부 벗는다는 1을 빼면 답이 나옴.