import sys
arr = [i for i in range(1,31)]
for _ in range(28): arr[int(sys.stdin.readline())-1] = 0
arr = filter(lambda x: x!=0, arr)
for i in arr: print(i)