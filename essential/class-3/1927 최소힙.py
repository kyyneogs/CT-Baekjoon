# 최소힙을 구현하기 위해서 파이썬에서 이미 구현되어 있는 우선순위 큐 라이브러리를 이용

# 이후에는 직접 코드를 작성해서 최소힙 문제를 다시 풀어봐야 할 것 같음.

import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    n = int(input())
    if n:
        heapq.heappush(heap, n)
    else:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print('0')