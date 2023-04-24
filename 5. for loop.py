"""


https://www.hackerrank.com/challenges/30-loops/problem?isFullScreen=true



"""

import math
import os
import random
import re
import sys


def table(n):
    for i in range(1, 11):
        if 1 <= i <= 10:
            t = n * i
            print(n, 'x', i, '=', t)


if __name__ == '__main__':
    n = int(input().strip())
    table(n)
