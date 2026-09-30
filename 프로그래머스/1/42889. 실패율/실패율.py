def solution(N, stages):
    length = len(stages)
    answer = []
    
    for i in range(1, N+1):
        count = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        length -= count
        answer.append((i, fail))
    
    answer.sort(key = lambda x : x[1], reverse=True)
    result = [i[0] for i in answer]
    return result