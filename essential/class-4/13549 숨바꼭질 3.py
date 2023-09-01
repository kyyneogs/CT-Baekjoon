import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * (K+2) if K>N else [0] * (N+2)

def BFS(start, end):
    que = deque()
    que.append(start)
    visited[start] = 1

    while(que):
        loc = que.popleft()
        if loc == end:
            return visited[end]-1
        for i, cost in ((-1,1), (loc,0), (1,1)):
            locn = loc + i
            if 0<= locn < len(visited) and not visited[locn]:
                visited[locn] += visited[loc] + cost
                que.append(locn)

print(BFS(N, K))