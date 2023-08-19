# 수의 갯수는 100 이하, 모든 수는 1,000 이하의 자연수

import sys

n = int(sys.stdin.readline())
arr = map(int, sys.stdin.readline().split())

result = 0

for i in arr:
    tmp = 0
    for j in range(1,i):
        if tmp>2: break
        else:
            if i%j==0: tmp = tmp+1
    if tmp==1: result = result+1

print(result)