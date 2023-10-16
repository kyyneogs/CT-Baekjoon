arr = [[1,1,1],[0,0,0],[0,1,0],[1,1,0]]

def gravity():
    m = len(arr[0])
    n = len(arr)
    for i in range(m):
        pointer = n-1
        for j in range(n-2, -1, -1):
            if arr[j][i]:
                tmp = arr[j][i]
                arr[j][i] = 0
                if not arr[pointer][i]:
                    arr[pointer][i] = tmp
                    pointer -= 1
                else:
                    pointer -= 1
                    arr[pointer][i] = tmp

def draw(arr):
    for k in arr:
        print(*k)
draw(arr)
gravity()
draw(arr)