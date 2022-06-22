from math import gcd

N, X = map(int, input().split())
X_LIST = list(map(int, input().split()))
ans = abs(X-X_LIST[0])
for i in range(1,N):
 a = abs(X-X_LIST[i])
 ans = gcd(ans,a)
print(ans)