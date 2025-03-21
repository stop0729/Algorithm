import heapq

def solution(scoville, K):
    q = []
    for i in range(len(scoville)):
        heapq.heappush(q, scoville[i])
    
    answer = 0
    while len(q) >= 2:
        first = heapq.heappop(q)
        if first >= K:
            return answer
        
        second = heapq.heappop(q)
        
        heapq.heappush(q, first + 2*second)
        answer += 1
    
    if q[0] >= K:
        return answer
    else:
        return -1