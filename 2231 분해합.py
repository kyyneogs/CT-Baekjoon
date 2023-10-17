N = int(input())

for i in range(N//2, N-1):
    tmp = 0
    for j in str(i):
        tmp += int(j)
    if i + tmp == N:
        print(i)
        exit()
print(0)