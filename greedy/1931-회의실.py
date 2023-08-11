N = int(input())
arr = []
for _ in range(N): arr.append(list(map(int, input().split())))
arr.sort(key= lambda x: (x[1]-x[0], x[0], -x[1]))
occupy = [1 for _ in range(max(arr, key=lambda x: x[1])[1]+1)]

cnt = 0
for i in arr:
    print(i, occupy)
    if occupy[i[0]] and occupy[i[1]-1]:
        for k in range(i[0], i[1]): occupy[k] = 0
        cnt = cnt+1
print(cnt)

# 반례 존재
# 5
# 0 3
# 2 4
# 3 6
# 5 7
# 6 9
# [o] 3
# [x] 2