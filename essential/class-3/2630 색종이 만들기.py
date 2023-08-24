import sys
input = sys.stdin.readline

def devide(x, y, N):
    color = arr[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != arr[i][j]:
                w1, b1 = devide(x, y, N//2)
                w2, b2 = devide(x+N//2, y, N//2)
                w3, b3 = devide(x, y+N//2, N//2)
                w4, b4 = devide(x+N//2, y+N//2, N//2)
                return w1+w2+w3+w4, b1+b2+b3+b4
    if color==0:
        return 1, 0
    else:
        return 0, 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in devide(0,0,N):
    print(i)