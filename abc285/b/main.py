N = int(input())
S = list(input())

for i in range(1,N):
  m = 0
  for j in range(N - i):
    if S[j] != S[j+i]:
      m = j + 1
    else:
      break
  print(m)