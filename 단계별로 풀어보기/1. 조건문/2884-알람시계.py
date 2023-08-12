import sys
H, M = map(int, sys.stdin.readline().split(' '))

M = M - 45
if M<0 : M, H = M+60, H-1
if H<0: H = H+24
print(H, M, sep=' ')