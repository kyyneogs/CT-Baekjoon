maxi = -1

def combination(stack, arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            stack.append(int(''.join(map(str, arr))))
            arr[i], arr[j] = arr[j], arr[i]

def dfs(arr, layer=1):
    global maxi
    stack = []
    combination(stack, arr)
    for i in stack:
        if layer==K:
            maxi = max(maxi, i)
            continue
        _arr = list(map(int, (str(i))))
        dfs(_arr, layer+1)

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = list(map(int, (str(N))))
    dfs(arr)
    print(f'#{tc} {maxi}')