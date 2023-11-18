import sys, math
input = sys.stdin.readline

N = int(input())
if N==1:
    print(0)
    exit()

array = [True for _ in range(N+1)]

for i in range(2, int(math.sqrt(N)+1)):
    if array[i]:
        j=2
        while i*j <= N:
            array[i*j] = False
            j+=1

deci = [0]
j=0
for i in range(2, N+1):
    if array[i]:
        deci.append(i+deci[j])
        j+=1

left, right, cnt = 0, 1, 0

while(right < len(deci)):
    tmp = deci[right] - deci[left]
    if tmp == N:
        cnt += 1
        right += 1
    elif tmp < N:
        right += 1
    elif tmp > N:
        left += 1

print(cnt)