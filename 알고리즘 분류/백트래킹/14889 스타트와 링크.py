import sys
from itertools import combinations
input = sys.stdin.readline

def calculate(buff_link):
    result = 0
    for i in range(N//2):
        for j in range(N//2):
            result += arr[buff[i]][buff[j]]
            result -= arr[buff_link[i]][buff_link[j]]
    return abs(result)

def backtracking(depth=0):
    if depth >= N//2:
        global mini
        buff_link = []
        for i in range(N):
            if i not in buff:
                buff_link.append(i)
        mini = min(mini, calculate(buff_link))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            buff.append(i)
            backtracking(depth+1)
            visited[i] = 0
            buff.pop()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
buff = []
mini = int(10e9)

backtracking()

print(mini)