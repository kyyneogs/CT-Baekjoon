import sys

N1, N2, N3 = map(int, sys.stdin.readline().split(' '))
if N1==N2==N3: print(10000 + 1000*N1)
elif (N1!=N2) and (N1!=N3) and (N2!=N3): print(100*(max(N1,N2,N3)))
else:
    if N2==N3: print(1000 + 100*N2)
    else: print(1000 + 100*N1)