import sys
arr, N = [], 9
for _ in range(N): arr.append(int(sys.stdin.readline()))
print(max(arr),arr.index(max(arr))+1,sep='\n')