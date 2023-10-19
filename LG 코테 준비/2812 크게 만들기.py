import sys
input = sys.stdin.readline

N, K = map(int, input().split())
x = input().rstrip()

stack = []
cnt = 0
for i in x:
    while stack and int(stack[-1]) < int(i) and cnt < K:
        stack.pop()
        cnt+=1
    stack.append(i)

if cnt < K:
    print("".join(stack[:-(K-cnt)]))
else:
    print("".join(stack))