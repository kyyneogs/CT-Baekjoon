import sys
input = sys.stdin.readline
N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
S = []
def DFS(start = 0, depth=0):
    if len(S)>=M:
        print(*S)
        return

    for i in range(0, N):
        if not arr[i] in S:
            S.append(arr[i])
            DFS(i+1, depth+1)
            S.pop()

DFS()