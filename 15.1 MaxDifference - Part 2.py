#MaximumSum of 1 pair from the list of an array:-
# Scope:-  best way to do is below 1st program because
# it does not use max()in built function:-


def maxsum(arr):
    max1 = 0
    max2 = 0
    for i in range(len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2 and arr[i] != max1:
            max2 = arr[i]
    return (max1 + max2)

arr = [1,3,5,6,9,9,4,2,7,10]
print(maxsum(arr))

def maxi_indexes(arr):
    n = len(arr)
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    x[0] = arr[0]

    if arr is None or n == 0:
        return 0

    for i in range(1, n):
        x[i] = y[i - 1] + arr[i]
        y[i] = max(y[i - 1], x[i - 1])

    return max(x[-1], y[-1])

print(maxi_indexes([2,3,2]))
print(maxi_indexes([4,3,6,8]))
