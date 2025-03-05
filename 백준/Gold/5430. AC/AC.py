from collections import deque
import json

T = int(input())

for i in range(T):
    order = input()
    num_D = 0
    for i in order:
        if i == 'D':
            num_D+= 1

    l = int(input())
    lst = input()

    if num_D > l:
        print('error')
        continue
    
    temp = deque(json.loads(lst))

    switch = 1
    num_R = 0
    for i in order:
        if i == "R":
            num_R += 1
            switch = switch * (-1)
        if i == 'D':
            if switch == 1:
                temp.popleft()
            else:
                temp.pop()

    temp = list(temp)
    if num_R % 2 == 0:
        print("[" + ",".join(map(str, temp)) + "]")
    else:
        temp.reverse()
        print("[" + ",".join(map(str, temp)) + "]")

