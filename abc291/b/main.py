N = int(input())
X = list(map(int, input().split()))
X.sort()
X = X[N:-N]
print(sum(X)/(N*3))