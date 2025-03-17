import sys

input = sys.stdin.readline

N = int(input().rstrip())

data = []
for i in range(N):
    data.append(list(map(int, input().split())))

data.sort(key = lambda x : x[0])    

result = 0
x, y = data[0]
tempx, tempy= x, y

for i in range(1,N):
    x, y = data[i]
    if x <= tempy:
        if tempy < y:
            tempy = y
        
    else:
        result += tempy - tempx
        tempx, tempy = x, y 

print(result + (tempy - tempx))