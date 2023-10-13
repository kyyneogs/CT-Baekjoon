arr = input().split('-')
sum = 0
for n, i in enumerate(arr):
    tmp = 0
    i = i.split('+')
    for j in i: tmp = tmp + int(j)
    if n==0: sum=tmp
    else: sum=sum-tmp
print(sum)