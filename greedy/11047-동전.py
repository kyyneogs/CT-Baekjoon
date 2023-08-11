N, K = map(int, input().split(' '))
money = []
for _ in range(N): money.append(int(input()))
money.reverse()

cnt = 0
for i in money:
    if K >= i:
        cnt = cnt + (K//i)
        K = K % i

print(cnt)