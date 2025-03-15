def post(node):
    
    if node.left != '.':
        post(node.left)
    if node.right != '.':
        post(node.right)

    print(node.item)

# 전위 순위 결과로부터 tree를 만들 수 있는가? -> 굳이 만들 필요 없이 배열로 받아서 생각하는듯
# 입력이 언제 끝나는지 어떻게 알아? try, except

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

data = []
while True:
    try:
        temp = int(input())
        data.append(temp)
    except:
        break


def pre_to_post(data):
    if len(data) == 0:
        return

    dataL, dataR = [], []

    mid = data[0]
    for i in range(1, len(data)):
        if mid < data[i]:
            dataL = data[1:i]
            dataR = data[i:]
            break
        if i == len(data) -1:
            dataL = data[1:]

    pre_to_post(dataL)
    pre_to_post(dataR)
    print(mid)

pre_to_post(data)