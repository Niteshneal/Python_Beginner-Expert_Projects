def get(m,r,c):
    sum = 0
    sum += m[r-1][c-1]
    sum += m[r-1][c+1]
    sum += m[r-1] [c]
    sum += m[r][c]
    sum += m[r+1][c-1]
    sum += m[r+1][c]
    sum += m[r+1][c+1]
    return sum
arr = []
for i in range(6):
    x = [int(arr_t) for arr_t in input().strip().split(' ')]
    arr.append(x)
max = -63
for i in range(1,5):
    for j in range(1,5):
        c = get(arr, i, j)
        if c > max:max = c
print(max)

#or Square Glass:-

def get(m, r, c):
    sum = 0
    sum+=m[r-1][c-1]
    sum+=m[r-1][c+1]
    sum+=m[r-1][c]
    sum+=m[r][c-1]
    sum+=m[r][c+1]
    sum+= m[r][c]
    sum+=m[r+1][c-1]
    sum+=m[r+1][c]
    sum+=m[r+1][c+1]
    return sum

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

max = -63
for m in range(1,5):
    for n in range(1,5):
        c = get(arr, m, n)
        if c > max:
            max = c
print(max)
