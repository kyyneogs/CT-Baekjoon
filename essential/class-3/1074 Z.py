# 패턴을 파악하여 브루트포스로 문제를 해결하면 시간복잡도 때문에 풀지를 못함
# 따라서, 분할정복을 이용해야함.

import sys
sys.setrecursionlimit(10000)

N, r, c = map(int, sys.stdin.readline().split())

def pattern(N, r, c, result=0):
    if N==0: return result
    else:
        result += 2*4**(N-1)*(r//(2**(N-1))) + 4**(N-1)*(c//(2**(N-1)))
        r = r - 2**(N-1)*(r//(2**(N-1)))
        c = c - 2**(N-1)*(c//(2**(N-1)))
        return pattern(N-1, r, c, result)

print(pattern(N, r, c))  