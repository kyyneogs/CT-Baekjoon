from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

def BFS(cnt=0, start=1):
    que = deque()
    que.append(start)
    visited[start] = 1
    while(que):
        n = que.popleft()
        cnt += 1
        for node in arr[n]:
            if not visited[node]:
                visited[node] = 1
                que.append(node)
    return cnt

for i in range(M):
    comp = input().split()
    if len(comp) >1:
        arr[int(comp[0])].append(int(comp[1]))
        arr[int(comp[1])].append(int(comp[0]))
        
print(BFS()-1)