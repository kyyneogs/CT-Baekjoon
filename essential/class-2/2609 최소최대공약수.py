n, m = map(int, input().split())
n, m = (m, n) if n < m else (n, m)

def uclidean(a, b):
    if a%b:
        k = uclidean(b, a%b)
    else: k = b
    return k

max_num = uclidean(n, m)
min_num = (n*m)//max_num

print(max_num, min_num, sep='\n')