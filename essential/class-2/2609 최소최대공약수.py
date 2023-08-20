# 유클라이드 호제법을 이용
# 최소공약수 * 최소공배수 = 두 수의 곱 이라는 규칙을 이용

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