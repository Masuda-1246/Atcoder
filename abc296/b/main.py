S = [list(input()) for _ in range(8)]
for i in range(8):
  for j in range(8):
    if S[i][j] == "*":
      print(chr(97+j), 8-i, sep="")
      exit()