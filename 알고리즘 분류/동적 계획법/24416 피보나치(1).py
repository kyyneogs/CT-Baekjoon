import sys
input = sys.stdin.readline
    
def fibo_dynamic(x):
    arr = [1, 1] + [0]*(x-2)
    for i in range(2, x):
        arr[i] = arr[i-1] + arr[i-2]
        cnt[1] += 1
    cnt[0] = arr[x-1]

N = int(input())
cnt = [0, 0]
fibo_dynamic(N)
print(' '.join(map(str, cnt)))