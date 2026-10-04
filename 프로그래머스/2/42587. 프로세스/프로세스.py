from collections import deque

def solution(priorities, location):
    q = []
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    q = deque(q)
    count = 0
    while q:
        prior, idx = q.popleft()
        if prior == max(priorities):
            count += 1
            if idx == location:
                return count
            priorities.remove(prior)
        else:
            q.append((prior, idx))
        
        
