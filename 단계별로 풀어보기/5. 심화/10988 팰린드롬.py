S = input().rstrip()
t = 1
for i in range(len(S)//2):
    if S[i]==S[-(i+1)]: t=t*1
    else: t=0
print(t)