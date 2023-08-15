# dleaf님 아이디어를 참고함

N = int(input())
M = 10000000

def slide(L,M):
    K = L%M//(M//10)
    # print(K)
    if M>10: return K + slide(L, M//10)
    else: return K

ans = 0
for i in range(1, N+1):
    if i+(i//M)+slide(i,M)==N:
    # if i+sum(list(map(int, str(i))))==N:
        ans = i
        break
print(ans)