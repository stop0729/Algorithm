import sys

input = sys.stdin.readline
M = int(input())
data = {i:False for i in range(1, 21)}
lst = []

for i in range(M):
    order = input().split()
    if len(order) == 2:
        order, num = order
        num = int(num)
        if order == 'add':
            data[num] = True
        elif order == 'remove':
            data[num] = False
        elif order == 'check':
            if data[num] == True:
                print(1)
            else:
                print(0)
        elif order == 'toggle':
            if data[num] == True:
                data[num] = False
            else:
                data[num] = True
    else:
        order = order[0]
        if order == 'all':
            data = {i:True for i in range(1, 21)}
        else:
            data = {i:False for i in range(1, 21)}