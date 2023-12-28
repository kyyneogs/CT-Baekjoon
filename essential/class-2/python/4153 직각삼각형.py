import sys

while(True):
    arr = list(map(int, sys.stdin.readline().split()))
    if arr == [0,0,0]: break
    arr.sort()

    if arr[2]*arr[2] == arr[0]*arr[0] + arr[1]*arr[1]:
        print('right')
    else: print('wrong')