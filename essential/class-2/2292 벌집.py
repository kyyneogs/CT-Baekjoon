N = int(input())-1

tmp = 0
k = 0
while tmp+6*k < N:
    tmp = tmp+6*k
    k += 1

print(k+1)