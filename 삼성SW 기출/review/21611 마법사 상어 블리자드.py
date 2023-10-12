N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
blizard = []
for _ in range(M):
    blizard.append(list(map(int, input().split())))

def destroy(board, d, s):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    counter = [0,0,0]
    nx, ny = N//2, N//2
    for _ in range(s):
        nx += dx[d-1]
        ny += dy[d-1]
        if board[nx][ny]:
            counter[board[nx][ny]-1] += 1
            board[nx][ny] = 0
    return counter

# 예는 이상 없다.
def spiral_to_line(board):
    # 가운데는 변환 안한다는 사실을 반드시 알아둬야함.
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    x, y, d = 0, N-1, 0
    line = []
    for i in range(N):
        line.append(board[0][i])
    for i in range(N-1):
        for _ in range(2):
            for _ in range(i, N-1):
                x += dx[d]
                y += dy[d]
                if x <0 or x>=N or y<0 or y>=N:
                    print(-1)
                    exit()
                line.append(board[x][y])
            d = (d+1)%4
    line.pop()
    line = line[-1::-1]
    return line

# 예도 이상 없음.
def line_to_spiral(board, line):
    # 가운데 빼고 입력 받으면 알아서 가운데 0을 포함시켜서 배열을 반환해줌!
    line = line[:N*N-1]
    line = line[-1::-1]
    tmp = [0] * (N**2-1-len(line))
    line = tmp + line + [0]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    x, y, d, idx = 0, N-1, 0, 0
    for _ in range(N):
        board[0][idx] =  line[idx]
        idx+=1
    for i in range(N-1):
        for _ in range(2):
            for _ in range(i, N-1):
                x += dx[d]
                y += dy[d]
                if x <0 or x>=N or y<0 or y>=N:
                    print(-1)
                    exit()
                board[x][y] = line[idx]
                idx += 1
            d = (d+1)%4
    return board

def move_line(line):
    pointer = 0
    for i in range(1,len(line)):
        if line[i] == 0:
            continue
        tmp = line[i]
        line[i] = 0
        if line[pointer] == 0:
            line[pointer] = tmp
            pointer += 1
        else:
            pointer += 1
            line[pointer] = tmp
    return line

def chain_destroy(line):
    stack = [0] # index append
    counter = [0,0,0]
    tmp = line[0]
    for i in range(1, len(line)):
        if line[i] == tmp:
            stack.append(i)
        else:
            if tmp != 0 and len(stack) >= 4:
                counter[tmp-1] += len(stack)
                for j in stack:
                    line[j] = 0
            tmp = line[i]
            stack = [i]
    if tmp != 0 and len(stack) >= 4:
        counter[tmp-1] += len(stack)
        for j in stack:
            line[j] = 0
    return line, counter

def chain_sum(line):
    new_line = []
    stack = [0]
    tmp = line[0]
    for i in range(1, len(line)):
        if line[i]==tmp:
            stack.append(i)
        else:
            new_line.extend([len(stack), tmp])
            tmp = line[i]
            stack = [i]
        if len(new_line) > N*N-1:
            return new_line
    if stack:
        new_line.extend([len(stack), tmp])
    return new_line

count = [0,0,0]
for i, j in blizard:
    destroy(board, i, j)
    line = spiral_to_line(board)
    line = move_line(line)
    while(True):
        line, tmp = chain_destroy(line)
        if sum(tmp) == 0: 
            break
        for i in range(3):
            count[i] += tmp[i]
        line = move_line(line)
    line = chain_sum(line)
    board = line_to_spiral(board, line)

sumi = 0
for i in range(3):
    sumi += count[i] * (i+1)
print(sumi)