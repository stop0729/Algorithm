m, n = map(int, input().split())

split1 = []
for i in range(1, m+1):
    if m % i == 0:
        split1.append(i)
        
split2 = []
for i in range(1, n+1):
    if n % i == 0:
        split2.append(i)
        
max_split = 0
for i in split1:
    if i in split2:
        if i > max_split:
            max_split = i
print(max_split)
print(int(m * n / max_split))