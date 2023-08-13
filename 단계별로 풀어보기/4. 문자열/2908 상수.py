N, S = map(list, input().rstrip().split())
N, S = N[2]+N[1]+N[0], S[2]+S[1]+S[0]
if int(N)>int(S): print(N)
else: print(S)