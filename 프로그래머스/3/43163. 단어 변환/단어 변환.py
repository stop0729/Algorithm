from collections import deque

def bfs(begin, target, words):
    q = deque()
    q.append([begin, 0])
    
    while q:
        now, step = q.popleft()
        
        if now == target:
            return step
        
        for word in words:
            temp = 0
            for i in range(len(word)):
                if word[i] != now[i]:
                    temp += 1
            
            if temp == 1:
                q.append([word, step+1])

def solution(begin, target, words):
    if target not in words:
        return 0
    answer = bfs(begin, target, words)
    return answer