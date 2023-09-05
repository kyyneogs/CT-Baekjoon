import sys
input = sys.stdin.readline

def DFS(ind):
    if visited[ind] == 1:
        return -1
    visited[ind] = 2

N = int(input())
arr = [0]+list(map(int, input().split()))
visited = [0] * (N+1)
result = [0]