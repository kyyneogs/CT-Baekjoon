# 내가 푸는 그리디 알고리즘의 가장 안좋음 점 : 단순화하여 생각 하질 못함, 문제의 본질을 꿰뚫질 못함.

# 우선, 현재 가용가능한 회의 중, 가장 일찍 시작하는 친구들을 선택해서 차근차근 넣어야겠지?

# (3,3) 을 먼저 고르는 것 보다는 (2,3)을 고르고 이후에 (3,3) 을 채우는 게 좋겠다.

import sys

N = int(sys.stdin.readline())
arr, occupy = [], []
for _ in range(N): arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort(key=lambda x: x[0])    # 시작시간 기준 정렬
arr.sort(key=lambda x: x[1])    # 종료시간 기준 정렬

cnt = 0
for i in range(N):
    if cnt:
        if arr[i][0] >= occupy[-1][1]: 
            occupy.append(arr[i])
            cnt = cnt+1
    else:
        occupy.append(arr[i])
        cnt = cnt+1

print(cnt)
# b_cnt = 0
# for _ in range(2):
#     cnt = 0
#     occupy = [1 for _ in range(max(arr, key=lambda x: x[1])[1]+1)]
#     for i in arr:
#         t = 1
#         # if occupy[i[0]] and occupy[i[1]-1]:
#         for j in range(i[0],i[1]): t = t * occupy[j]
#         if t:
#             for k in range(i[0], i[1]): occupy[k] = 0
#             cnt = cnt+1
#         # print(i, occupy)
#     if cnt > b_cnt : b_cnt = cnt
#     arr.sort(key= lambda x: (x[1]-x[0], x[0]))
# print(b_cnt)

# 반례 존재
# 5
# 0 3
# 2 4
# 3 6
# 5 7
# 6 9
# [o] 3
# [x] 2