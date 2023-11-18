import sys
input = sys.stdin.readline

A = " " + input().rstrip()
B = " " + input().rstrip()
LCS = [[0 for _ in range(len(A))] for _ in range(len(B))]

result = 0
for i in range(1,len(A)):
    for j in range(1,len(B)):
        if A[i]==B[j]:
            LCS[j][i] = LCS[j-1][i-1] + 1
        else:
            LCS[j][i] = max(LCS[j][i-1], LCS[j-1][i])
        if result < LCS[j][i]:
            result = LCS[j][i]

print(result)