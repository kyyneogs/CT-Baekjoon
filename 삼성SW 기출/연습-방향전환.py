UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

R, C = 4, 4
arr = [[0]*R for _ in range(R)]

def get_loc(i, j, speed, direct):
    if direct in [UP, DOWN]:
        cycle = R*2-2
        if direct == UP:
            speed += 2 * (R-1) -i
        else:
            speed += i
        speed %= cycle
        if speed >= R:
            return (cycle-speed, j, UP)
        return (speed, j, DOWN)
    
a, b, d = get_loc(1, 1, 7, UP)
print(a, b, d)