import sys
arr, cnt, K = [], 0, 42
for i in range(10): arr.append(int(sys.stdin.readline())%K)
print(len(set(arr)))