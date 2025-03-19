s = []
result = 0
cnt = 0

def dfs(dungeons, start, l, k, visited):
    global result, cnt
    result = max(result, cnt)
    
    for i in range(start, l):
        if k >= dungeons[i][0] and visited[i] == False:
            k -= dungeons[i][1]
            cnt += 1
            visited[i] = True
            dfs(dungeons, start, l, k, visited)
            cnt -= 1
            k += dungeons[i][1]
            visited[i] = False

    return result
        

def solution(k, dungeons):
    l = len(dungeons)
    visited = [False] * l
    answer = dfs(dungeons, 0, l, k, visited)
    return answer