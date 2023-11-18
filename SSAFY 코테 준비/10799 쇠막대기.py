import sys
input = sys.stdin.readline

iron = input().rstrip()
result = 0
cnt = 0

for i in range(len(iron)):
    if iron[i]=='(':
        cnt += 1
    else:
        cnt -= 1
        if iron[i-1]=='(':
            result += cnt
        else:
            result += 1
print(result)