# 내가 생각해보는 로직 :
# 우선, 모든 랜선 n개의 값을 다 더하고, 자르고자 하는 개수 m개만큼 잘라서 그 지점부터 스타트
# 1씩 줄여가며 검사, 만약 m개를 딱 맞추는 조건을 달성한다 -> break로 탈출
# 가장 높은 수 부터 시작하므로, 가장 빨리 끝난 값이 최댓값이다.

# 이 방법은 근데 시간복잡도가 최대 N^2인것 같은데...

# 방법을 돌려보자 -> 이분탐색으로..?



import sys
n, m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]

front, end = 1, max(arr)

while(front<=end):
    mid = (front+end)//2
    sum = 0
    for i in arr:
        sum += i//mid
    
    if sum>=m:
        front = mid + 1
    else:
        end = mid - 1
print(end)