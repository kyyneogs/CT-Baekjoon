import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

indegree = [-1] + [0]*N
direct = [[] for _ in range(N+1)]
que = deque()

for _ in range(M):
    A, B = map(int, input().split())
    indegree[B] += 1
    direct[A].append(B)
    pass

for i in range(1, N+1):
    if not indegree[i]:
        que.append(i)

while(que):
    student = que.popleft()
    print(student, end=' ')
    for i in direct[student]:
        indegree[i] -= 1
        if not indegree[i]:
            que.append(i)
