import sys
input = sys.stdin.readline

N = int(input())
pos_col = [False]*N
queen = set()

def check(row, col):
    if not row:
        return True

    for rown, coln in queen:
        slope = (coln-col)/(rown-row)
        if slope == -1.0 or slope == 1.0:
            return False
    return True

def DFS(row=0, result=0):
    for col in range(N):
        if pos_col[col]:
            continue

        if check(row, col):
            queen.add((row,col))
            pos_col[col] = True
            if row<N-1:
                result = DFS(row+1, result)
            else:
                result += 1
                queen.discard((row, col))
                pos_col[col] = False
                return result
            queen.discard((row, col))
            pos_col[col] = False
    return result

print(DFS())