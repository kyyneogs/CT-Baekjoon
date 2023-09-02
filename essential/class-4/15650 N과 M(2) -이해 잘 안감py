import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = []

def DFS(start=1):
    if len(S) >= M:
        print(*S)
        return

    for i in range(start, N+1):
        # if i not in S:
            S.append(i)
            DFS(i+1)
            S.pop()
DFS()