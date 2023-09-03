import sys
input = sys.stdin.readline

N = int(input())
table = list(map(int, input().split()))
mem = [0]

for i in table:
    if i > mem[-1]:
        mem.append(i)
    else:
        left, right = 0, len(mem)
        while(left<right):
            mid = (left+right)//2
            if mem[mid]<i:
                left = mid+1
            else:
                right = mid
        mem[right] = i
print(len(mem)-1)

# for i in table:
#     if i > mem[-1]:
#         mem.append(i)
#     else:
#         mem.append(i)
#         mem.sort()
#         mem.pop()

# print(len(mem)-1)

