import sys
from itertools import combinations
input = sys.stdin.readline

def calculate(a, b):
    result = 0
    for i in range(N//2):
        for j in range(N//2):
            result += arr[a[i]][a[j]]
            result -= arr[b[i]][b[j]]
    return abs(result)

N = int(input())
sample_list = [i for i in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]
mini = int(10e9)
combi = list(combinations(sample_list, N//2))

for i in combi:
    j = list(filter(lambda x: x not in i, sample_list))
    mini = min(mini, calculate(i, j))

print(mini)
