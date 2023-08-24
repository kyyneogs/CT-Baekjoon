import sys

N, M = map(int, sys.stdin.readline().split())

dictionary = {}

for i in range(N):
    name = sys.stdin.readline().rstrip()
    dictionary[name] = i+1
    dictionary[str(i+1)] = name

for j in range(M):
    print(dictionary[sys.stdin.readline().rstrip()])