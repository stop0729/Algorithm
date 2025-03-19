def solution(clothes):
    dict = {}
    
    for i in clothes:
        if i[1] not in dict:
            dict[i[1]] = 1
        else:
            dict[i[1]] += 1
    
    answer = 1
    
    for i in dict:
        answer = answer * (dict[i]+1)
        
    answer = answer - 1
    return answer