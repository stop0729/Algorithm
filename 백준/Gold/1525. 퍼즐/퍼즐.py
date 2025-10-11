from collections import deque
import sys

move = [(-1,0), (1,0), (0,1), (0, -1)]
dist = dict()

start = ""
for i in range(3):
    a = str(input())
    for j in a:
        if j != " ":
            start += j
dist[start] = 0

def bfs():
    que = deque()
    que.append(start)

    while que:
        x = que.popleft()
        if x == "123456780":
            return dist[x]
        temp = x.find('0')
        a, b = temp//3, temp%3

        for i in range(4):
            na, nb = a + move[i][0], b + move[i][1]
            if 0<= na <3 and 0<= nb <3:
                new_temp = na*3 + nb
                new_x = list(x)
                new_x[temp], new_x[new_temp] = new_x[new_temp], new_x[temp]
                new_x = ''.join(new_x)
                if new_x not in dist:
                    dist[new_x] = dist[x] + 1
                    que.append(new_x)

    return -1

print(bfs())