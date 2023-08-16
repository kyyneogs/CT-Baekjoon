import sys
N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append([])
    K = sys.stdin.readline().rstrip()
    for j in K: arr[i].append(1 if j=='W' else -1)

min = 8*8

for i in range(N-8+1):
    for j in range(M-8+1):
        for m in [1,-1]:
            flag = arr[i][j]*-1*m
            tmp = 0
            for k in range(i,i+8):
                for l in range(j,j+8):
                    if arr[k][l]*flag==True: tmp=tmp+1
                    flag = flag*-1
                flag = flag*-1
            if min > tmp: min=tmp

print(min)