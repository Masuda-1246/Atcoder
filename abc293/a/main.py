S = input()
ans = []
i = 0
for _ in range(int(len(S)/2)):
  ans.append(S[i+1])
  ans.append(S[i])
  i+=2
print(*ans, sep='')