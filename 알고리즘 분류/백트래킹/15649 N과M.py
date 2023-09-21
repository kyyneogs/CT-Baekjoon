import sys
input = sys.stdin.readline

def backtracking(x, k, length):
    for i in range(1, x+1):
        if i not in k:
            k.append(i)
            if len(k) >= length:
                print(' '.join(map(str, k)))
            else:
                backtracking(x, k, length)
            k.pop()

N, M = map(int, input().split())
backtracking(N, [], M)