N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
maxi = 0

def check(line):
    for i in range(1,N):
        if abs(line[i]-line[i-1])>1:
            return False
        
        if line[i] < line[i-1]:
            for j in range(L):
                if i+j >= N or line[i] != line[i+j] or slope[i+j]:
                    return False
                if line[i] == line[i+j]:
                    slope[i+j] = 1
        
        if line[i] > line[i-1]:
            i -= 1
            for j in range(L):
                if i-j < 0 or line[i] != line[i-j] or slope[i-j]:
                    return False
                if line[i] == line[i-j]:
                    slope[i-j] = 1
    return True 

# check row
for i in range(N):
    slope = [0] * N
    if check([arr[i][j] for j in range(N)]):
        maxi += 1

# check col
for j in range(N):
    slope = [0] * N
    if check([arr[i][j] for i in range(N)]):
        maxi += 1

print(maxi)