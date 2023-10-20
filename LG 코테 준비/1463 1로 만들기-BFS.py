from collections import deque

N = int(input())
arr = [0]*(N+1)
que = deque()
que.append(N)

while(que):
    x = que.popleft()
    if x == 1: break

    if x%3 == 0 and arr[x//3] == 0:
        arr[x//3] = arr[x]+1
        que.append(x//3)
    
    if x%2 == 0 and arr[x//2] == 0:
        arr[x//2] = arr[x]+1
        que.append(x//2)
    
    if arr[x-1] == 0:
        arr[x-1] = arr[x]+1
        que.append(x-1)

print(arr[1])