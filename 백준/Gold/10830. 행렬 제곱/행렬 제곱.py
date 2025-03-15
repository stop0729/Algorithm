N, B = map(int, input().split())
data1 = [list(map(int, input().split())) for i in range(N)]

def mul(data1, data2):
    data3 = []
    N = len(data1)
    M = len(data1[0])
    K = len(data2[0])

    for i in range(N):
        lst = []
        for j in range(K):
            temp = 0
            for k in range(M):
                temp += data1[i][k] * data2[k][j]
            lst.append(temp % 1000)
        data3.append(lst)

    return data3

def square(data, B):
    if B == 1:
        for i in range(len(data)):
            for j in range(len(data)):
                data[i][j] %= 1000
        return data
    
    q = B // 2
    temp = square(data, q)
    
    if B % 2 == 0:
        return mul(temp, temp)
    else:
        return mul(mul(temp, temp), data)
    
result = square(data1, B)
l = len(result)

for i in range(l):
    for j in range(l):
        print(result[i][j], end = ' ')
    print()


""""
1 2
3 4
5 6

-1 -2 0
0 0 3

"""