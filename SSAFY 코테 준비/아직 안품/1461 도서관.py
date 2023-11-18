import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
positive, negative = [], []
for i in arr:
    if i > 0: positive.append(i)
    else: negative.append(-i)
positive.sort(reverse=True)
negative.sort(reverse=True)

cnt = 0
for i in range(0, len(positive), M):
    cnt += 2*positive[i]
for j in range(0, len(negative), M):
    cnt += 2*negative[j]

if not positive: cnt -= negative[0]
elif not negative: cnt -= positive[0]
else: cnt -= max(negative[0], positive[0])
print(cnt)