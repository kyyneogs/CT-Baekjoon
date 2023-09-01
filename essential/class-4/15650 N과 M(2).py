import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def DFS(start=1):
    if start == N+1:
        return
    for i in range(start+1,N+1):
        print(start, i, sep=' ')
    DFS(start+1)

DFS()