import heapq

n, k = map(int, input().split())

stone = []
for i in range(n):
    s_w, price = map(int, input().split()) # 무게, 가격
    stone.append((s_w, price))

bag = []
for i in range(k):
    w = int(input())
    bag.append(w)

bag.sort(reverse=True)
stone.sort(key = lambda x:x[0], reverse=True)
q = []

answer = 0

while bag:
    b_w = bag.pop()

    while stone:
        s_w, price = stone.pop()

        if b_w >= s_w:
            heapq.heappush(q, (-price))
        else:
            stone.append((s_w, price))
            break
    if q:
        answer += -heapq.heappop(q) # 우선순위 q가 비어있을 상황 즉 어떤 보석도 지금 가방에 못들어갔을때

print(answer)