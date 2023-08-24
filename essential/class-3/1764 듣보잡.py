import sys

N, M = map(int, sys.stdin.readline().split())
dictionary = {}
for _ in range(N):
    dictionary[sys.stdin.readline().rstrip()] = 0

result = []
for _ in range(M):
    string = sys.stdin.readline().rstrip()
    if dictionary.get(string) != None:
        result.append(string)

result.sort()
print(len(result))
for i in result:
    print(i)