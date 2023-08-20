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