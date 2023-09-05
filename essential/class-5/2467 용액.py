import sys
input = sys.stdin.readline
INF = int(10e9)

N = int(input())
arr = list(map(int, input().split()))
left, right, maxi = 0, N-1, INF
result = (left, right)

while(left<right):
    sumi = arr[left] + arr[right]

    if abs(sumi) <= maxi:
        result = (left, right)
        maxi = abs(sumi)
        if not sumi:
            break
    
    if sumi < 0:
        left += 1
    else:
        right -= 1

print(arr[result[0]], arr[result[1]], sep=' ')