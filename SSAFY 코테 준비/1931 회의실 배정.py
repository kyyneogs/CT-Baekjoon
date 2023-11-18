import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x:(x[1], x[0]))
que = []

heapq.heappush(que, -arr[0][1])

for i,j in arr[1:]:
    if i >= -que[0]:
        heapq.heappush(que, -j)

print(len(que))