# 시간복잡도 = 50^4

import sys

n, m = map(int, sys.stdin.readline().split())

table, check_table = [], ['WBWBWBWB' if i%2==0 else 'BWBWBWBW' for i in range(8)]

for i in range(n):
    table.append(sys.stdin.readline().strip())

min_ = []

for i in range(n-7):
    for j in range(m-7):
        min1, min2 = 0,0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if table[k][l] == check_table[k-i][l-j]: min1 = min1 + 1
                else: min2 = min2 + 1
        min_.extend((min1, min2))

print(min(min_))