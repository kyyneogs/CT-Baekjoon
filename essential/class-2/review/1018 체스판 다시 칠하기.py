import sys
input = sys.stdin.readline
INF = int(1e9)

M, N = map(int, input().split())
table = [input().rstrip() for _ in range(M)]
check_table = ['WBWBWBWB' if i%2==0 else 'BWBWBWBW' for i in range(8)]

mini = INF
for xx in range(M-7):
    for yy in range(N-7):
        minw, minb = 0, 0
        for x in range(8):
            for y in range(8):
                # 입력 받은 테이블은 0+xx ~ 7+xx, 0+yy ~ 7+yy 까지, 전체 테이블에 대해서 8x8로 잘라서 나누어 확인
                # 체크 테이블은 항상 0~7, 0~7 까지 고정범위
                if table[xx+x][yy+y] != check_table[x][y]:
                    minw += 1
                else:
                    minb += 1
        mini = min(mini, minw, minb)

print(mini)