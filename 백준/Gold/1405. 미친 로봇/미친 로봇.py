num, e, w, s, n = map(int, input().split())

direction = [e, w, s, n]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

graph = [[0] * (2*num+1) for _ in range(2*num+1)]
graph[num][num] = 1


answer = 0

def dfs(x, y, cnt, percent):
    global answer

    if cnt == num:
        answer += percent
        return
    
    now_percent = percent

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < 2*num+1 and 0<= ny < 2*num+1:
            if graph[nx][ny] == 1:
                continue

            else:
                graph[nx][ny] = 1
                cnt += 1
                dfs(nx, ny, cnt, now_percent * direction[i] / 100)
                graph[nx][ny] = 0
                cnt -= 1

    return answer

result = dfs(num, num, 0, 1)

print(result)