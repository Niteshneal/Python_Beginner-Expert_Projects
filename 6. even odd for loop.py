n = int(input())

for i in range(n):
    s = input()
    even = ''
    odd = ''

    for j in range(len(s)):
        if j % 2 == 0:
            even += s[j]
        else:
            odd += s[j]
    print(even, '-', odd)
