N, K = map(int, input().split())

comp = set(['a', 'n', 't', 'i', 'c'])
new_str = set()
ans = 0

word = []

for i in range(N):
    tmp = input()
    word.append(tmp)
    tmp = tmp[4:-4]
    for i in tmp:
        if i not in comp:
            new_str.add(i)

new_str = list(new_str)

def check():
    result = 0
    for i in word:
        flag = True
        for k in i:
            if k not in comp:
                flag = False
                break
        if flag == True:
            result += 1

    return result


def dfs(start, depth):
    global ans
    if depth == K - 5:
        ans = max(ans, check())
        return
    
    for i in range(start, len(new_str)):
        comp.add(new_str[i])
        dfs(i+1, depth+1)
        comp.remove(new_str[i])

if K < 5:
    print(0)
elif K == 26 or K-5 > len(new_str):
    print(N)
else:
    dfs(0, 0)
    print(ans)