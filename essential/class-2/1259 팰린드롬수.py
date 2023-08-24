# 이거 해시맵을 활용하면 훨씬 빠르게 작성이 가능할 지도?

import sys

while(True):
    line = sys.stdin.readline().rstrip()
    if line =='0': break

    start, end = 0, len(line)-1
    while(True):
        if start>=end:
            print('yes')
            break
        elif line[start] != line[end]:
            print('no')
            break
        else:
            start = start+1
            end = end-1