N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))
    
arr.sort(reverse=True)


temp = set()
for i in range(N):
    for j in range(N):
        temp.add(arr[i] + arr[j])

def solve():
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] - arr[j] in temp:
                return arr[i]
            
answer = solve()
print(answer)