import sys
INF = int(1e9)
input = sys.stdin.readline

N, S = map(int, input().split())

table = [0] + list(map(int, input().split()))

for i in range(N):
    table[i+1] += table[i]

left, right = 0, 1
mini = INF

while(right <= N):
    if table[right] - table[left] < S:
        right += 1
    else:
        cnt = right - left
        mini = cnt if cnt < mini else mini
        left +=1

print(mini if not mini==INF else '0')