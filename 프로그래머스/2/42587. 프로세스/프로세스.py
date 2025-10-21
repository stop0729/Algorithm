from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    count = 0

    while q:
        mx = max(q)
        tmp = q.popleft()

        if tmp == mx:
            count += 1  # 출력된 문서 수
            if location == 0:
                return count
            else:
                location -= 1
        else:
            q.append(tmp)
            if location == 0:
                location = len(q) - 1
            else:
                location -= 1