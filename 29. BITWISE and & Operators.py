def bitwiseAnd(N, K):
    # Write your code here
    max_bit = 0
    for i in range(1, N+1):
        for j in range(1, i):
            bit = i & j
            if max_bit < bit < K:
                max_bit = bit
                if max_bit == K-1:
                    return max_bit
    return max_bit
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nk = input().rstrip().split()
        N = int(nk[0])
        K = int(nk[1])
        print(bitwiseAnd(N, K))

