board = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], \
         [12], [13], [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], \
            [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]
scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, \
         38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]

dices = list(map(int, input().split()))
maxi = 0
horses = [0,0,0,0]

def dfs(score=0, layer=0):
    global maxi
    if layer>=10:
        maxi = max(maxi, score)
        return

    for i in range(4):
        x = board[horses[i]][-1]
        for _ in range(1, dices[layer]):
            x = board[x][0]
        
        if x==32 or (x<32 and x not in horses):
            before = horses[i]
            horses[i] = x
            dfs(score + scores[x], layer+1)
            horses[i] = before

dfs()
print(maxi)