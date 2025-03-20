from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(start, maps):
    q = deque()
    q.append(start)
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < len(maps) and 0<= ny < len(maps[0]) and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append([nx, ny])

def solution(maps):
    bfs([0, 0], maps)
    if maps[len(maps)-1][len(maps[0])-1] == 1:
        answer = -1
    else:
        answer = maps[len(maps)-1][len(maps[0])-1]
        
    print(maps)
    
    return answer