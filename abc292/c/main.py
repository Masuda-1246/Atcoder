N = int(input())
ans=0
cnt = [0]*(N+1)
for i in range(1, N+1):
  for j in range(i, N+1, i):
    cnt[j] += 1
for AB in range(1,N):
  CD = N-AB
  ans += cnt[AB]*cnt[CD]
print(ans)