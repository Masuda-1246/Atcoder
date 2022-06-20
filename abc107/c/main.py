N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = float('inf')
for i in range(N-K+1):
  l = A[i]
  r = A[i+K-1]
  ans = min(ans, abs(l)+abs(l-r), abs(r)+abs(r-l))
print(ans)