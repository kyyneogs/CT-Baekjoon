import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = [1]*N

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        x1, y1 = arr[i]
        x2, y2 = arr[j]

        if x1 < x2 and y1 < y2:
            answer[i] += 1

print(' '.join(map(str, answer)))