import sys
input = sys.stdin.readline

symbols = {')':'(', '}':'{', ']':'['}

while(True):
    line = input().rstrip()
    if line == '.': break

    stack = []
    for i in line:
        if i == '.': break

        if i in ('(', ')', '{', '}', '[', ']'):

            if i in symbols and stack and stack[-1] == symbols[i]:
                stack.pop()
            else:
                stack.append(i)

    if stack:
        print('no')
    else:
        print('yes')