S = input().rstrip()
arr = [-1 for _ in range(26)]
for i, j in enumerate(S):
    if arr[ord(j)-97]==-1: arr[ord(j)-97] = i
print(*arr)