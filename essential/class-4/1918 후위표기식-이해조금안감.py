string = input().rstrip()
result = ''
stack = []

for s in string:
    if s >= 'A' and s<='Z': result += s
    elif s=='(': stack.append(s)
    elif s=='*' or s=='/':
        while stack and (stack[-1]=='*' or stack[-1]=='/'): result += stack.pop()
        stack.append(s)
    elif s=='+' or s=='-':
        while(stack and stack[-1]!='('): result += stack.pop()
        stack.append(s)
    elif s==')':
        while(stack and stack[-1]!='('): result += stack.pop()
        stack.pop()
while(stack): result += stack.pop()
print(result)