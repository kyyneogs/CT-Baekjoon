import sys

N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    stack = [[1,0],[0,1]]
    for i in range(num+1):
        if i > 1:
            stack[i%2][0] += stack[(i+1)%2][0] 
            stack[i%2][1] += stack[(i+1)%2][1]
    print(*stack[num%2])