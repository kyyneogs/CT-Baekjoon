# 데이터의 개수는 최대 1,000,000개, 범위는 -1,000,000 ~ 1,000,000
# 데이터가 어떤 형식인지 모름 -> 따라서, 최악의 경우 nlogn 을 초과하는 시간복잡도를 가지는 정렬 알고리즘 사용불가.
# 정수형식의 데이터이므로, 부호를 나눠서 계수정렬을 사용하면 될 것 같음.

# Tlqkf 리스트의 모든 원소가 정수인 경우에는 파이썬에서 알아서 계수정렬을 하는 듯 하다...

import sys
arr = [[],[]]

N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    if num < 0:
        arr[0].append(-1*num)
    else:
        arr[1].append(num)

count = [([0] * max(arr[0])) if len(arr[0])>0 else [], ([0] * (max(arr[1])+1)) if len(arr[1])>0 else []]

for i in arr[0]:
    count[0][i-1] += 1

for i in arr[1]:
    count[1][i] += 1

for i in range(len(count[0])-1, -1, -1):
    for j in range(count[0][i]):
        print(-1*(i+1))

for i in range(len(count[1])):
    for j in range(count[1][i]):
        print(i)