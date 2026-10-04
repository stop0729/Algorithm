def solution(clothes):
    comb = {}
    for i in clothes:
        if i[1] in comb:
            comb[i[1]] += 1
        else:
            comb[i[1]] = 1
    
    answer = 1
    
    for i in comb:
        answer = answer * (comb[i]+1)
    answer -= 1
    return answer