graph = []
for i in range(10):
    graph.append(list(map(int, input().split())))

    
def determine(x, y, c):
    nx, ny = x + c, y + c
    for i in range(x, nx+1):
        for j in range(y, ny+1):
            if graph[i][j] == 0:
                return False
    return True

def attach(x, y, c, value):
    for i in range(x, x+c+1):
        for j in range(y, y+c+1):
            graph[i][j] = value
            
def glue(p):
    global result
    for x in range(10):
        for y in range(10):
            if graph[x][y] == 1:
                for c in range(5):
                    nx, ny = x + c, y + c
                    if group[c] and ny < 10 and nx < 10:
                        if determine(x, y, c):
                            attach(x, y, c, 0)
                            group[c] -= 1
                            glue(p+1)
                            group[c] += 1
                            attach(x, y, c, 1)
                return
    result = min(result, p)
                    
group = [5, 5, 5, 5, 5]
result = 26
glue(0)
if result == 26:
    print(-1)
else:
    print(result)