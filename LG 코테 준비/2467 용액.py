import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left, right = 0, N-1
mini = int(10e9)
answer = []
while(left < right):
    tmp = arr[left]+arr[right]
    if abs(tmp) < mini:
        mini = abs(tmp)
        answer = [arr[left], arr[right]]
    
    if tmp < 0:
        left += 1
    else:
        right -= 1
print(" ".join(map(str, answer)))