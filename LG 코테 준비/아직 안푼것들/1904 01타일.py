import sys
input = sys.stdin.readline

N = int(input())
arr = [1] + [2] + [0] * (N-2)

for i in range(2, N):
    arr[i] = (arr[i-1] + arr[i-2]) % 15746

print(arr[N-1])