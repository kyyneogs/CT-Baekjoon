import sys
input = sys.stdin.readline

def backtracking(x, length, k):
    if length <= len(k):
        print(' '.join(map(str, k)))
        return
    for i in range(1, x+1):
        if not k or k[-1] <= i: 
            k.append(i)
            backtracking(x, length, k)
            k.pop()

N, M = map(int, input().split())
backtracking(N, M, [])