from collections import deque

def rotate_right(x, d):
    if x>=5 or gears[x-1][2] == gears[x][6]:
        return
    
    rotate_right(x+1, -d)
    gears[x].rotate(d)

def rotate_left(x, d):
    if x<=0 or gears[x+1][6] == gears[x][2]:
        return
    
    rotate_left(x-1, -d)
    gears[x].rotate(d)

gears = {}
for i in range(1,5):
    gears[i] = deque(list(map(int, input())))

N = int(input())
for _ in range(N):
    x, d = map(int, input().split())

    rotate_right(x+1, -d)
    rotate_left(x-1, -d)
    gears[x].rotate(d)

sumi = 0
for i in range(4):
    sumi += gears[i+1][0] * 2**i
print(sumi)