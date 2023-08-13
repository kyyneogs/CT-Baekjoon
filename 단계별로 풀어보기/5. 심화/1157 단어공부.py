arr = [0 for _ in range(26)]
S = input().upper()
for i in S: arr[ord(i)-65] = arr[ord(i)-65]+1
if arr.count(max(arr))>1: print('?')
else: print(chr(arr.index(max(arr))+65))