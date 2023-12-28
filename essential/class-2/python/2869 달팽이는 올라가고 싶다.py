import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

CNT = (V-A) // (A-B)
V -= (A-B)*CNT

if A >= V:
    CNT += 1
else:
    CNT += 2

print(CNT)