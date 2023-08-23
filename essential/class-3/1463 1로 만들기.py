from collections import deque
que = deque()

N = int(input())
visited = [0 for _ in range(N+1)]

visited[N] = 1
que.append(N)

while(que):
    K = que.popleft()

    if K%3==0 and not visited[K%3]:
        visited[K%3] += 1
        que.append(K%3)
    elif K%2==0 and not visited[K%2]:
        visited[K%2] += 1
        que.append(K%2)
    elif K-1!=0 and not visited[K-1]:
        visited[K-1] += 1
        que.append(K-1)

print(visited[1])