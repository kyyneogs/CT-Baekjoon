import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

N, M = map(int, input().split())
parent = [i for i in range(N)]

arr = [list(map(int, input().split())) for _ in range(M)]

result = 0
for i, tmp in enumerate(arr):
    a, b = find_parent(tmp[0]), find_parent(tmp[1])
    if a!=b:
        union_parent(a, b)
    else:
        result = i+1
        break
print(result)