from collections import deque

N, K = map(int, input().split())
convbelt = deque(list(map(int, input().split())))
robot = deque([0]*N)
r_c = 0
c_c = 0
cnt = 0

while(True):
    convbelt.rotate(1)
    robot.rotate(1)
    if robot[-1]:
        robot[-1] = 0
        r_c -= 1
    if r_c:
        for i in range(N-2, -1, -1):
            if robot[i] and not robot[i+1] and convbelt[i+1]:
                robot[i+1] = 1
                robot[i] = 0
                convbelt[i+1] -= 1
                if not convbelt[i+1]:
                    c_c += 1
        if robot[-1]:
            robot[-1] = 0
            r_c -= 1
    if not robot[0] and convbelt[0]:
        r_c += 1
        robot[0] = 1
        convbelt[0] -= 1
        if not convbelt[0]:
            c_c += 1
    cnt += 1
    
    if c_c >= K:
        break

print(cnt)