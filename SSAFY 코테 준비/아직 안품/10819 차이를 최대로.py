import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
visited = [0]*N
maxi = 0
stack = []

def bctrk(layer):
    global maxi
    if layer==N:
        score = 0
        for i in range(N-1):
            score += abs(stack[i]-stack[i+1])
        maxi = max(maxi, score)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            stack.append(arr[i])
            bctrk(layer+1)
            stack.pop()
            visited[i] = 0

bctrk(0)
print(maxi)