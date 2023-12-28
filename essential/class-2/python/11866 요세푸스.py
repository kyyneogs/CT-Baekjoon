from collections import deque

n, k = map(int, input().split())
arr = deque([i for i in range(1, n+1)])
result = []
while(len(arr)):
    for i in range(k-1):
        arr.append(arr.popleft())
    result.append(arr.popleft())

print('<', end='')
print(*result, sep =', ', end='>')