arr = [int(input()) for _ in range(3)]
dic = {}
for i in range(10): dic[str(i)] = 0

sumi = arr[0]*arr[1]*arr[2]
for i in str(sumi): dic[i] += 1
for i in dic.values(): print(i)