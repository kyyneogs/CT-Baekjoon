import sys
input = sys.stdin.readline
MAX_NUM = 1000000

N = int(input())
card = [0] * (MAX_NUM+1)
score = [0] * (MAX_NUM+1)
player_card = list(map(int, input().split()))
for i in player_card:
    card[i] = 1

for i in player_card:
    j = i
    while(j<MAX_NUM+1):
        if i!=j and card[j]:
            score[i] += 1
            score[j] -= 1
        j += i

for i in player_card:
    print(score[i], end=' ')