N,T = map(int, input().split())
CT = [list(map(int, input().split())) for _ in range(int(N))]
ans = 1010
for c,t in CT:
  if t <= T:
    ans = min(ans,c)
print(ans if ans!=1010 else "TLE")