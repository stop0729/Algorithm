N = int(input())
lst = list(map(int, input().split()))
a, b, c, d, e, f = lst

# 3면 합 최소 구하기
three_min = min(d+b, b+c, c+e, e+d) + min(a, f)

# 2면 합 최소
two_min = min(d+b, b+c, c+e, e+d, a+d, a+b, a+c, a+e, f+b, f+c, f+d, f+e)

a = 4
if N == 2:
    b = N**3 - 4
    c = 0
    print(min(lst)*(c) + (two_min*b) + (three_min)*(a))

elif N == 1:
    print(sum(lst) - max(lst))

else:
    b = (N-1)*4 + (N-2) * 4
    c = (N-1) * (N-2) * 4 + (N-2) ** 2
    print(min(lst)*(c) + (two_min*b) + (three_min)*(a))

