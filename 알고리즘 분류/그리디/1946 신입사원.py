import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()
    maxi = N
    temp = arr[0][1]

    for i in range(1, N):
        if arr[i][1] < temp:
            temp = arr[i][1]
        
        else:
            maxi -= 1
    
    print(maxi)