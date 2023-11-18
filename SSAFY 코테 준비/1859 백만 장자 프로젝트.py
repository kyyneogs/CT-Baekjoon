T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxi, sumi, tmpi = 0, 0, 0

    for i in range(N-1, -1, -1):
        if arr[i] >= maxi:
            maxi = arr[i]
            sumi += tmpi
            tmpi = 0
        else:
            tmpi += maxi - arr[i]
    sumi += tmpi
    print(f'#{tc} {sumi}')