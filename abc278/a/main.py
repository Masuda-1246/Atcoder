N, K = map(lambda x: int(x), input().split())
A = list(map(lambda x: int(x), input().split()))
A = A[K:]
zero = [0 for _ in range(K if K < N else N)]
ans = A+zero
print(*ans, sep=" ")