from collections import deque

temp = input()
q = deque()

for i in range(len(temp)):
    q.append(temp[i])

    if len(q)>=4:
        if str(q[-1])+str( q[-2]) + str(q[-3] + str(q[-4])) == 'PAPP':
            for _ in range(4):
                q.pop()
            q.append('P')



if len(q) == 0:
    print('PPAP')
elif len(q) == 1:
    if q[0] == ('P'):
        print('PPAP')
    else:
        print('NP')
else:
    print('NP')