import sys
n, r = map(int, sys.stdin.readline().split())

def factorial(a, b):
    ans = 1
    for i in range(b):
        ans *= a
        a -= 1
    return ans

if r > (n//2): r = n-r

print(factorial(n,r)//factorial(r,r))