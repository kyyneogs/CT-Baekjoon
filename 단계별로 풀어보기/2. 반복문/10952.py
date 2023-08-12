import sys
arr = []
while(True): 
    arr.append(list(map(int, sys.stdin.readline().split(' '))))
    if arr[-1][0]==0 and arr[-1][1]==0: break
for i in arr[0:-1]: print(i[0]+i[1])