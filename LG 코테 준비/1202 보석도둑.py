import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())
que, jewerlys = [], []
for _ in range(N):
    heapq.heappush(jewerlys, list(map(int, input().split())))
bags = [int(input()) for _ in range(K)]
bags.sort()

answer = 0
for i in range(K):
    while jewerlys and bags[i] >= jewerlys[0][0]:
        heapq.heappush(que, -heapq.heappop(jewerlys)[1])
    if que:
        answer += -heapq.heappop(que)

print(answer)