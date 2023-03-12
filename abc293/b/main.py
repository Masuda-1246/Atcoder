N = int(input())
A = list(map(int, input().split()))

B = {i:True for i in range(1, N+1)}
ans = []

for i in range(1, N+1):
  if B[i] :
      B[A[i-1]] = False

for i, v in enumerate(B):
  if B[v]:
    ans.append(v)

print(len(ans))
print(*ans)

