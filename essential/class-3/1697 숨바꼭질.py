# 반복문을 이용해서 코드 최적화를 진행해야 좋을 것 같음.
# 최대 값의 범위를 200001 이 아니라, 100001 로 설정해서 최대한 적게 코드를 실행시켜야 하긴 하는데
# 100002 와 같은 값이 될 수 없는 이유는 모르겠음.
# 이건 아마 반례가 나오면 바뀔 수도 있지 않을까 싶음.

# 50001 -> 100002로 가는것보다, 50001 에서 그냥 1을 빼고 두배 곱하는것이 최대임.
# 따라서, 이전 케이스ㅓ에서 한번 빼버리고 곱하는게 더 효율적이라 1000002를 넘길 필요 자체가 없는 듯 함.

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

MAX_RANGE = 100001

que = deque()
visited = [0 for _ in range(MAX_RANGE)]

que.append(N)

while(que):
    location = que.popleft()
    if location==M:
        break
    
    for next in (location-1, location+1, location*2):
        if 0 <= next < MAX_RANGE and not visited[next]:
            que.append(next)
            visited[next] = visited[location]+1

print(visited[location])