import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N): arr.append(list(map(int, sys.stdin.readline().split(' '))))
for i in range(N): print(f'Case #{i+1}: {arr[i][0]} + {arr[i][1]} = {arr[i][0]+arr[i][1]}')