import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    arr = [[0]*(N+1) for _ in range(K+1)]
    for i in range(1,N+1):
        arr[0][i] = i
    
    for i in range(1, K+1):
        temp = 0

        for j in range(1, N+1):
            temp += arr[i-1][j]
            arr[i][j] = temp
    
    print(arr[K][N])