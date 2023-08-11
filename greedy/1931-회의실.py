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