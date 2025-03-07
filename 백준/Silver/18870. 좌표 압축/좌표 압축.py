N = int(input())
data = list(map(int, input().split()))
set_data = list(set(data))
set_data.sort()

dict = {value : index for index, value in enumerate(set_data)}

for i in range(len(data)):
    print(dict[data[i]], end= ' ')