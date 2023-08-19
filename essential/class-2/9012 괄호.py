import sys
N = int(sys.stdin.readline())

for _ in range(N):
    ps = sys.stdin.readline().rstrip()
    stack = 0
    M = len(ps)

    for s in ps:
        if stack<0: break
        elif s=='(': stack=stack+1
        else: stack=stack-1
    
    if stack==0: print('YES')
    else: print('NO')