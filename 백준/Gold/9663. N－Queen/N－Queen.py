N = int(input())

isused1 = [0] * 40
isused2 = [0] * 40
isused3 = [0] * 40
result = 0

def func(row):
    global result

    if row == N:
        result += 1
        return
    for col in range(N):
        if (isused1[col] or isused2[row+col] or isused3[row-col+N-1]):
            continue
        isused1[col] = 1
        isused2[row+col] = 1
        isused3[row-col+N-1] = 1
        func(row+1)
        isused1[col] = 0
        isused2[row+col] = 0
        isused3[row-col+N-1] = 0
        
func(0)
print(result)