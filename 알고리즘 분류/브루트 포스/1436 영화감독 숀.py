N = int(input())
number = 666
cnt = 0

while(cnt<N):
    count_6 = 0
    string = str(number)
    for i in range(len(string)-2):
        if string[i:i+3]=='666': count_6 = count_6+1
    if count_6>=1: cnt=cnt+1
    number = number+1
print(number-1)