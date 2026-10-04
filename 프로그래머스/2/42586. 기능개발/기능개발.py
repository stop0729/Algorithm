from collections import deque

def solution(progresses, speeds):
    q = deque()
    for i in range(len(progresses)):
        q.append([100 - progresses[i], speeds[i]])
    
    answer = []
    while q:
        count = 0
        tmp = q[0]
        if tmp[0] % tmp[1] == 0:
            day = tmp[0] // tmp[1]
        else:
            day = tmp[0] // tmp[1] + 1
        
        for i in q:
            i[0] = i[0] - i[1] * day
        print(q)
        
        while q:
            if q[0][0] <= 0:
                q.popleft()
                count += 1
            else:
                break
        
        answer.append(count)
    return answer