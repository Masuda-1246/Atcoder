H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]

for i in range(H):
  ans = []
  for j in range(W):
    if A[i][j] == 0:
      ans.append('.')
    else:
      ans.append(chr(64+A[i][j]))
  print(*ans, sep="")