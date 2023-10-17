import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
new_arr = [-1]*N

for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        new_arr[stack.pop()] = arr[i]
    stack.append(i)

print(' '.join(map(str, new_arr)))