H, W = map(int, input().split())

S_list = [list(input()) for _ in range(H)]

for i in range(H):
  S = S_list[i]
  for j in range(1,W):
    if S[j-1] == "T" and S[j] == "T":
      S[j-1] = "P"
      S[j] = "C"
  print(*S,sep="")
