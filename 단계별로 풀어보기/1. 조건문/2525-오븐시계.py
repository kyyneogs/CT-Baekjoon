import sys

H, M = map(int, sys.stdin.readline().split(' '))
K = int(sys.stdin.readline())
K1, K2 = K//60, K%60

H, M = H+K1, M+K2
if M >= 60: H, M = H+1, M-60 
if H >= 24: H = H-24

print(H, M, sep=' ')