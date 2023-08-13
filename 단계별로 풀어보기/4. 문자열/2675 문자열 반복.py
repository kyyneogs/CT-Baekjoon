import sys
N = int(sys.stdin.readline())
for _ in range(N):
    K, S = sys.stdin.readline().rstrip().split()
    for i in S: print(i*int(K), end='')
    print('')