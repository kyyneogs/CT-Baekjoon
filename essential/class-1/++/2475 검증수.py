arr = list(map(int, input().split()))

sumi = 0
for i in arr: sumi += i**2
print(sumi%10)