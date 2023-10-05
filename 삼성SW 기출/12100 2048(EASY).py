import sys
from collections import deque
input = sys.stdin.readline

def move(direction, arr, cnt=0):
    for i in range(1,N):
        pointer = 0
        for j in range(N):
            tmp = arr[i][j]
            if tmp:


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]