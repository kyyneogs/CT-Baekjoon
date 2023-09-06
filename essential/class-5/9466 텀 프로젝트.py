import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def DFS(ind, depth=0):
    depth += 1
    if visited[arr[ind]] == 1:
        visited[ind] = 1
        visited[arr[ind]] = 1
        return depth
    
    if visited[arr[ind]] == 2:
        visited[ind] = 1
        visited[arr[ind]] = 1
        stack.append(arr[ind])
        return depth-1
    visited[ind] = 2
    depth = DFS(arr[ind], depth)

    if stack:
        if stack[0]==ind:
            stack.pop()
        visited[ind] = 1
        return depth-1
    else:
        visited[ind] = 1
        return depth

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0]+list(map(int, input().split()))
    visited = [0] * (N+1)
    stack = []
    result = 0

    for i in range(1, N+1):
        if not visited[i]:
            result += DFS(i)
    print(result)