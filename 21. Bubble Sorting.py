import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

x = 0

for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            x += 1
            a[j] = a[j + 1]
            a[j + 1] = a[j]

print("Array is sorted in " + str(x) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))
