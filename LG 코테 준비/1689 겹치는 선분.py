import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int ,input().split())) for _ in range(N)]
que = []

arr.sort(key = lambda x:x[0])
heapq.heappush(que, arr[0][1])

for i in range(1, len(arr)):
    if que[0] > arr[i][0]:
        heapq.heappush(que, arr[i][1])
    else:
        heapq.heappop(que)
        heapq.heappush(que, arr[i][1])

print(len(que))