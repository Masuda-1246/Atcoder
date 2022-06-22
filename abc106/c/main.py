S = list(map(int,input()))
K = int(input())
for i in range(K):
  if S[i] != 1:
    print(S[i])
    quit()
  if i == len(S)-1:
    break
print(1)
  