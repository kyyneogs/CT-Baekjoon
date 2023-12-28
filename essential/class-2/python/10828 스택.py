import sys
from collections import deque

N = int(sys.stdin.readline())
stack =  deque()
for i in range(N):
    string = sys.stdin.readline().rstrip()
    if string[0:4] == 'push':
        _, n = string.split()
        stack.append(int(n))
    elif string == 'pop': print(stack.pop() if len(stack) else '-1')
    elif string == 'size': print(len(stack))
    elif string == 'empty': print('0' if len(stack) else '1')
    elif string == 'top': print(stack[len(stack)-1] if len(stack) else '-1')