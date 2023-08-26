arr = list(map(int, input().split()))
for i in range(1,8):
    if arr[i]-1 == arr[i-1]: string = 'ascending'
    elif arr[i]+1 == arr[i-1]: string = 'descending'
    else:
        string='mixed'
        break
print(string)