import math
import os
import random
import re
import sys

n = int(input().strip())

arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr1 = []

for i in range(n):
    arr1.append(arr[n - i - 1])

s = ''
for i in range(len(arr1)):
    s += str(arr1[i]) + ' '

print(s)

n = int(input().strip())

arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr1 = []

for i in range(n):
    arr1.append(arr[n - i - 1])

print(' '.join(str(i) for i in arr1))

