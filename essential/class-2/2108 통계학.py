import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
maxi = max(arr)
mini = min(arr)
print(round(sum(arr)/N))
print(arr[N//2])
nums = [0]*(maxi+1)
for i in arr:
    nums[i] += 1
tmaxi = max(nums)
tarr = []
for i in range(1, maxi):
    if nums[i] == tmaxi:
        tarr.append(i)
tarr.sort()
print(tarr)
print(tarr[0] if len(tarr)==1 else tarr[1])
print(maxi - mini)