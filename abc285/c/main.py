S = list(input())
S.reverse()
ans = 0
for i in range(len(S)):
  ans += (ord(S[i])-64)*26**i
print(ans)