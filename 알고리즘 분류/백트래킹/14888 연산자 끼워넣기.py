import sys
input = sys.stdin.readline

def get_operate(x, i, depth):
    if i==0: return x + arr[depth]
    elif i==1: return x - arr[depth]
    elif i==2: return x * arr[depth]
    else: return int(x / arr[depth])

def backtracking(x, depth = 1):
    if depth >= N:
        result[0] = max(result[0], x)
        result[1] = min(result[1], x)
        return
    
    for i in range(4):
        if operator[i]:
            operator[i] -= 1
            backtracking(get_operate(x, i, depth), depth+1)
            operator[i] += 1

N = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))
result = [-int(10e9), int(10e9)]

backtracking(arr[0])
print(" ".join(map(str, result)))