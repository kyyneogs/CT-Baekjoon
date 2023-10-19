N = int(input())
if N < 18:
    k = 1
else:
    k = N - len(str(N))*9

for i in range(k, N-1):
    tmp = sum([int(j) for j in str(i)])
    if i + tmp == N:
        print(i)
        exit()
print(0)