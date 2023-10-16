arr = [1,2,3,4]
visited = [0]*4

def permutations(n, new_arr):
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            permutations(n, new_arr + [arr[i]])
            visited[i] = 0

def combinations(n, new_arr, c=0):
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return
    
    for i in range(c, len(arr)):
        combinations(n, new_arr+[arr[i]], i)

# permutations(2, [])
combinations(2, [])
