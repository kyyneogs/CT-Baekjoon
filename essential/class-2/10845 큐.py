import sys
from collections import deque

N = int(sys.stdin.readline())
que =  deque()
for i in range(N):
    string = sys.stdin.readline().split()
    if string[0] == 'push': que.append(int(string[1]))
    elif string[0] == 'pop': print(que.popleft() if len(que) else '-1')
    elif string[0] == 'size': print(len(que))
    elif string[0] == 'empty': print('0' if len(que) else '1')
    elif string[0] == 'front': print(que[0] if len(que) else '-1')
    elif string[0] == 'back': print(que[len(que)-1] if len(que) else '-1')