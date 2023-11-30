# without DP, use count of combinations(factorial)
import sys
input = sys.stdin.readline

def factorial(x, target=1):
    if x <= target:
        return 1
    else:
        return x * factorial(x-1, target)

TC = int(input())

for _ in range(TC):
    N, M = map(int, input().split())
    print(factorial(M, M-N)//factorial(N))