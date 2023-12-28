N = int(input())

for i in range(N//5, -1, -1):
    j = (N-5*i)//3
    if 5*i + 3*j == N:
        print(i+j)
        exit()

print(-1)