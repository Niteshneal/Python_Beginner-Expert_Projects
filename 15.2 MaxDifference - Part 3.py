#without space complexity:-

def maxi_indexes(arr):
    n = len(arr)
    x = arr[0]
    y = 0

    if arr is None or n == 0:
        return 0

    for i in range(1, n):
        x = y + arr[i]
        y =  max(y, x)

    return max(x, y)

print(maxi_indexes([2,3,2]))
print(maxi_indexes([4,3,6,8]))
