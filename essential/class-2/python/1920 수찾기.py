# N, M 은 최대 100,000 까지.
# N^2이상은 사용 불가

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
M = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

def find(num):
    front, end = 0, N-1

    while(front <= end):
        middle = (front + end)//2
        if num == arr[middle]:
            return 1
        elif num < arr[middle]:
            end = middle - 1
        else:
            front = middle + 1
    return 0

for i in number:
    print(find(i))