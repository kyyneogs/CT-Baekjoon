N = int(input())

min = 999999

for i in range(N//5,-1,-1):
    number = N-5*i
    cnt = i + number//3
    number = number%3
    if number==0 and min>cnt: 
        min=cnt
        break

print(min if min!=999999 else -1)