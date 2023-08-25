import sys
input = sys.stdin.readline

command = {'add':0, 'remove':1, 'check':2, 'toggle':3, 'all':4, 'empty':5}
S = set()

M = int(input())
for _ in range(M):
    cmd = input().split()
    if len(cmd)>1: num = int(cmd[1])
    cmd[0] = command[cmd[0]]
    if cmd[0]==0:
        S.add(num)
    elif cmd[0]==1:
        S.discard(num)
    elif cmd[0]==2:
        print(1 if num in S else 0)
    elif cmd[0]==3:
        S.discard(num) if num in S else S.add(num)
    elif cmd[0]==4:
        S = set([i for i in range(1,21)])
    else:
        S = set()