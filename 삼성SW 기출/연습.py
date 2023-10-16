# arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]

# N, M = len(arr), len(arr[0])

# length = 3
# new_arr = [[0]*length for _ in range(length)]

# def draw(arr):
#     for i in arr:
#         print(*i)

# def rotate(sx,sy,length):
#     new_arr = [[0]*N for _ in range(N)]
#     for i in range(sx, sx+length):
#         for j in range(sy, sy+length):
#             ox, oy = i - sx, j - sy
#             x, y = length - ox - 1, oy
#             new_arr[y+sx][x+sy] = arr[i][j]
#     draw(new_arr)
#     for i in range(sx, sx+length):
#         for j in range(sy, sy+length):
#             arr[i][j] = new_arr[i][j]

# rotate(2, 1, 2)
# draw(arr)

arr = [[[] for _ in range(3)] for _ in range(3)]