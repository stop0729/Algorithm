a, b, c = map(int, input().split())

def mul(a, b, c):
    if b == 1:
        return a % c
    val = mul(a, b//2, c)
    val = val * val % c
    if b%2 == 0:
        return val
    return val * a % c
        
result = mul(a,b,c)
print(result)