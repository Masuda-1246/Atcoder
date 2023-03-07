N, M = map(lambda x: int(x), input().split())
S = [list(input()) for _ in range(N)]
ans = 0
for i in range(N):
  for j in range(i+1,N):
    sum = 0
    for k in range(M):
      if S[i][k]=="o" or S[j][k]=="o":
        sum+=1
    if sum==M:
      ans+=1
print(ans)