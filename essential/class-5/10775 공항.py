import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x):
    parent[x] = x-1

G = int(input())
P = int(input())
planes = [int(input()) for _ in range(P)]
parent = [i for i in range(G+1)]
result = 0
for plane in planes:
    gate = find_parent(plane)
    if not gate:
        break
    union_parent(gate)
    result += 1
print(result)