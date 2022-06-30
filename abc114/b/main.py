S = list(map(int,input()))
ans = 1000
for i in range(len(S)-2):
  ans = min(ans,abs(753 - (100*S[i]+10*S[i+1]+S[i+2])))

print(ans)