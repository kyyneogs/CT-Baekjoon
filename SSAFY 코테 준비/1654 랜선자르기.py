import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

left, right = 1, max(arr)

while left<=right:
    middle = (left+right)//2
    cnt = 0

    for i in arr:
        cnt += i//middle
    
    if cnt < K:
        right = middle-1
    else:
        left = middle+1

print(right)