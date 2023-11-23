import sys
input = sys.stdin.readline

N = int(input())

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort()
arrB.sort(reverse=True)
result = 0

for i in range(N): result += arrA[i]*arrB[i]

print(result)