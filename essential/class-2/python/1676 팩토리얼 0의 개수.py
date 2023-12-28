N = int(input())
K = 1
for i in range(1,N+1):
    K *= i

K = list(map(int, str(K)))
answer = 0

for i in range(len(K)-1, -1, -1):
    if K[i] != 0:
        break
    answer += 1

print(answer)