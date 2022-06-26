N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))
dA = {i+1:A[i] for i in range(len(A))}

for l in L:
  if (l+1<=K):
    if dA[l] + 1 < dA[l+1]:
      dA[l] += 1
  else:
    if dA[l] + 1 <= N:
      dA[l] += 1

answer = []
for i in range(len(dA)):
  answer.append(dA[i+1])
  
print(*answer)