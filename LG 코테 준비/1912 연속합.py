import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))

for i in range(1,N+1):
    arr[i] = max(arr[i], arr[i]+arr[i-1])

print(max(arr[1:]))