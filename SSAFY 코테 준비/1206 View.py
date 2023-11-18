dy = [1, 2, -1, -2]

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    for i in range(2,N-2+1):
        for height in range(arr[i]+1):
            for j in range(4):
                if height <= arr[i+dy[j]]:
                    break
            else:
                cnt+=1
    
    print(f'#{tc} {cnt}')