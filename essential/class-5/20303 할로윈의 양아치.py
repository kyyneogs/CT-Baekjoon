import sys
import heapq
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a, b = (a, b) if a>b else (b, a)
    parent[a] = b

def count_parent(x, cnt=0):
    if parent[x] != x:
        visited[x] = cnt+1
        count_parent(parent[x], cnt+1)
    else:
        visited[x] = cnt+1

N, M, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
relation = [tuple(map(int, input().split())) for _ in range(M)]
parent = [i for i in range(N+1)]
visited = [0] * (N+1)

for a, b in relation:
    a, b = find_parent(a), find_parent(b)
    if a!=b:
        union_parent(a, b)

candys = []

for i in range(N, 0, -1):
    if parent[i] == i:
        visited[i] += 1
        candys.append((visited[i], arr[i]))
    else:
        visited[i] += 1
        visited[parent[i]] += 1
        arr[parent[i]] += arr[i]

# candys.sort(key = lambda x: (x[0], x[1]))
DP = [0] * (K+1)

for i in range(len(candys)):
    child, candy = candys[i]
    for j in range(K, child-1, -1):
        DP[j] = max(DP[j-child] + candy, DP[j])

print(DP[K-1])
