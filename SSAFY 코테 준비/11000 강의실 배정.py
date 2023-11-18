import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

que = [arr[0][1]]

for i,j in arr[1:]:
    if que[0] <= i:
        heapq.heappop(que)
    heapq.heappush(que, j)

print(len(que))