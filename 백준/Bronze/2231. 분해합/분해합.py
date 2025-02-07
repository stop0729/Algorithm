a = int(input())

for i in range(1, a+1):
    temp = i
    str_i = str(i)
    for j in range(len(str_i)):
        temp += int(str_i[j])
        
    if temp == a:
        print(i)
        break
    if i == a:
        print('0')
        break