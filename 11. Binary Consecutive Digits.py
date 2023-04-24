def bin(n):
    min = 0
    max = 0
    for i in range(n):
        remainder = n % 2
        if remainder == 1:
            min += 1
            if min > max:
                max = min
        else:
            min = 0
        n = n // 2
    return max

n = int(input(": "))
print(bin(n))
