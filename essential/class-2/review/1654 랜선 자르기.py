import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

front, end = 1, max(arr)
while(front<=end):
    mid = (front+end)//2
    sumi = 0
    # 각 랜선에 대해서 중간값으로 나누어지는 랜선의 갯수를 누적합.
    for i in arr:
        sumi += i//mid
    # 랜선의 총 갯수가 N보다 같거나 크게 되면, 아직 더 크게 자를 수 있음을 의미
    if sumi >= N:
        front = mid + 1
    else:
        end = mid - 1

print(end)