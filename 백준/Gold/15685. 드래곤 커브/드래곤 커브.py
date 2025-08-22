graph = [[0]*101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())

for i in range(n):
    x, y, d, g = map(int, input().split())
    temp = [[x, y], [x+dx[d], y+dy[d]]]

    for _ in range(g):

        a, b = temp[-1]

        for j in range(len(temp)-2, -1, -1):
            c, d = temp[j]
            c = c - a
            d = d - b # 끝점 기준으로 회전할것이기에 빼줌1

            new_coordi = [-d+a, c+b] # 90도 회전하고 끝점을 다시 더해줌
            if 0<= -d+a and -d+a <=100 and 0<= c+b and c+b <=100:
                temp.append(new_coordi)
        
    for j in temp:
        a, b = j
        graph[b][a] = 1


answer = 0 
for i in range(len(graph)-1):
    for j in range(len(graph)-1):
        if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] and graph[i+1][j+1]:
            answer += 1

print(answer)



