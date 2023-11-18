import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jews = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
jews.sort(reverse=True)
bags.sort()

que = []
result = 0

for bag in bags:
    while jews and jews[-1][0] <= bag:
        heapq.heappush(que, -jews.pop()[1])
    if que:
        result += -heapq.heappop(que)

print(result)