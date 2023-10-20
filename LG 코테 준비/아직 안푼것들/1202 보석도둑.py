import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jew = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
jew.sort()
bags.sort()

tmp = []
result = 0
for bag in bags:
    while jew and bag>=jew[0][0]:
        heapq.heappush(tmp, -jew[0][1])
        heapq.heappop(jew)
    if tmp:
        result += heapq.heappop(tmp)
    elif not jew:
        break

print(-result)


# while(jew and bags):
#     price, weight = heapq.heappop(jew)
#     price = -price

#     for i in range(len(bags)):
#         if weight <= bags[i]:
#             bags.pop(i)
#             result += price
#             break

# print(result)




# for i in range(N):
#     j1, j2 = heapq.heappop(jew)
#     j1, j2 = -j1, -j2
#     print(j1, j2)

# que = [list(map(int, input().split())) for _ in range(N)]
# que.sort(reverse=True,key=lambda x:x[1])
# que = deque(que)

# bags = [int(input()) for _ in range(K)]
# bags.sort()
# result = 0
# while(que):
#     weight, price = que.popleft()
#     for i in range(len(bags)):
#         if weight < bags[i]:
#             bags[i] = -1
#             result += price
#             break
# print(result)