# hello

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def cleaning(x, y, d):
    # 0:북 1:동 2:남 3:서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    result = 0
    back_flag = False

    while(True):
        if not back_flag:   # back flag가 올라간 경우
            if arr[x][y]==0:
                arr[x][y] = 2
                result += 1
            for i in range(d-1, d-5, -1):
                nx, ny = x+dx[i], y+dy[i]

                if arr[nx][ny]==0:
                    x, y, d = nx, ny, (i+4)%4
                    break

                if i==d-4:
                    back_flag = True
                    x, y = x-dx[d], y-dy[d]
        else:
            if arr[x][y]==1:
                return result
            else:
                back_flag = False

print(cleaning(x, y, d))