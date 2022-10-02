N, S = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(int(N))]
dp= [[0] * (S+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
  a, b = ab[i-1]
  for j in range(S+1):
    if dp[i-1][j] == 0:
      continue
    if j + a <= S:
      dp[i][j+a] = 1
    if j + b <= S:
      dp[i][j+b] = 1
if dp[-1][-1] == 0:
  print("No")
else:
  print("Yes")
  ans = []
  p = S
  for i in range(N-1, -1, -1):
    a,b = ab[i]
    if dp[i][p-a]:
      ans.append('H')
      p -= a
    elif dp[i][p-b]:
      ans.append('T')
      p -= b
  ans.reverse()
  print(*ans, sep='')