import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    sumi, streak = 0, 0
    ox = input().rstrip()
    for i in ox:
        if i=='O':
            streak += 1
            sumi += streak
        else:
            streak = 0
    print(sumi)