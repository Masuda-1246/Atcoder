N, M = map(int, input().split())
B = [[False]*N for _ in range(N)]
for _ in range(M):
    k, *X = map(int, input().split())
    for i in range(k):
        for j in range(i+1, k):
            B[X[i]-1][X[j]-1] = True
print(B)
for i in range(N):
    for j in range(i+1, N):
        print(not B[i][j])
        if not B[i][j]:
            print('No')
            exit()
print('Yes')
