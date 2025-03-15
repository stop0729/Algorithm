# 각 칸마다 C개의 대문자 알파벳 True, False 기록
# dfs를 시작해서 칸마다 지정. 만약 더이상 갈곳이 없다면 그때 True의 개수를 기록하고 전부 False로
import sys
input = sys.stdin.readline

R, C = map(int, input().split())

data = []
for _ in range(R):
    data.append(list(input().strip())) 

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

nap = set()
nap.add(data[0][0])
result = 0

def dfs(x, y):
    global result, nap

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx <= R-1 and 0<= ny <= C-1:
            if data[nx][ny] not in nap:
                nap.add(data[nx][ny])
                dfs(nx, ny)

    if result < len(nap):
        result = len(nap)
    nap.remove(data[x][y])

dfs(0, 0)

print(result)