import sys
input = sys.stdin.readline

string = input().rstrip()
boom = input().rstrip()

while boom in string:
    string = string.replace(boom, "", len(string))

print(string) if string else print("FRULA")