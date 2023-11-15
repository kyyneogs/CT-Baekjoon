# 제출번호 54316563 작성자 puranium235 코드 참조함.
# https://www.acmicpc.net/source/54316563

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = [i for i in range(N)]
    priorities = list(map(int, input().split()))
    que = deque([[i,j] for i,j in zip(priorities, arr)])
    priorities.sort(reverse=True)

    cnt = 0
    for priority in priorities:
        while(que[0][0] != priority):
            que.append(que.popleft())
        
        cnt += 1
        if que[0][1] == M:
            break
        que.popleft()
        
    print(cnt)