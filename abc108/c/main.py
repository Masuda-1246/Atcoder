N, K = map(int, input().split())
ans = 0
ans1 = 0
for i in range(1,N+1):
  if i % K == 0:
    ans += 1
  elif i % (K/2) == 0:
    ans1 += 1
ans = ans**3
ans1 = ans1**3
print(ans + ans1 if (K %2 == 0) else ans)
