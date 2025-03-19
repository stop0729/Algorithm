from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

data = [list(input()) for _ in range(5)]

def is_available(s):
    l = [i for i in s]
    
    q = deque([l[0]])
    l.remove(l[0])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if [nx, ny] in l:
                l.remove([nx, ny])
                q.append([nx, ny])
    if len(l) == 0:
        return True
    return False

n = []
s = []
result = 0

# 25개중 조합 찾는 문제라 했지.     
def dfs(start):
    global result
    if len(n) == 7:
        if n.count('S') >= 4 and is_available(s):
            result += 1
        return
    
    else:
        for i in range(start, 25):
            q, r = i//5, i%5
            n.append(data[q][r])
            s.append([q, r])
            dfs(i+1)
            n.pop()
            s.pop()

dfs(0)
print(result)