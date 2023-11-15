import sys
input = sys.stdin.readline

N = int(input())
answer = []
stack = []
start_num = 1
flag = False

for _ in range(N):
    num = int(input())

    if flag:
        continue

    while start_num <= num:
        stack.append(start_num)
        answer.append('+')
        start_num += 1
    
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        answer = ['NO']
        flag = True

for i in answer:
    print(i)