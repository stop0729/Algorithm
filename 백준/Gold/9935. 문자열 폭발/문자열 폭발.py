from collections import deque

A = input()
B = input()
l = len(B)

q = []

flag = 0
for i in range(len(A)):
    q.append(A[i])
    temp = ''.join(q[-l:])
    if temp == B:
        for i in range(l):
            q.pop()


if len(q) == 0:
    print("FRULA")
else:
    print(''.join(q))