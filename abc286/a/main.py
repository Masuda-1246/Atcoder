N, P, Q, R, S = map(int, input().split())
A = input().split()
diff = R-P
ans = []
for i in range(len(A)):
  if P-1 <= i and i <= Q-1:
    ans.append(A[i+diff])
  elif R-1 <= i and i <= S-1:
    ans.append(A[i-diff])
  else:
    ans.append(A[i])
print(*ans)