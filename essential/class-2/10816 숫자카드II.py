# 데이터의 범위를 따지면 N^2이상의 알고리즘을 사용하는 것은 불가능.
# 따라서 해시 알고리즘을 이용해서 최대한 빠르게 찾아야함.
# 파이썬에서의 딕셔너리는 기본적으로 해시 알고리즘을 사용.
# 따라서, 이분탐색 혹은 순차탐색보다 훨씬 빠르다.
# 이분탐색을 사용하려면, 최악의 경우에도 N*K의 시간복잡도를 유지하는 계수정렬을 이용하여 정렬해야함.
# 데이터값이 어떻게 되어있는지 모르니, 퀵정렬을 이용하면 최악의 경우에 N^2 이상의 시간복잡도를 가지니 주의해야함.

import sys
_ = sys.stdin.readline()
arr1 = map(int, sys.stdin.readline().split())
_ = sys.stdin.readline()
arr2 = map(int, sys.stdin.readline().split())

hash_ = {}

for i in arr1:
    if i in hash_:
        hash_[i] += 1
    else:
        hash_[i] = 1

print(" ".join(str(hash_[k]) if k in hash_ else '0' for k in arr2))