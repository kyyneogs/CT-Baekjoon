import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    seq = (N-1)//H+1
    floor = (N-1)%H+1
    print(100*floor+seq)