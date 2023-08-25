import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
que = deque()

for _ in range(m):
    i, j = map(int, input().split())
    arr[i].append(j)
    arr[j].append(i)

def BFS(start):
    if visited[start]: return 0

    que.append(start)
    visited[start] = 1
    while(que):
        ind = que.popleft()
        for node in arr[ind]:
            if not visited[node]:
                visited[node] = 1
                que.append(node)
    return 1

sumi = 0
for i in range(1,n+1):
    sumi += BFS(i)

print(sumi)