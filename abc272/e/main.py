N,M = map(lambda x: int(x), input().split())
A = list(map(lambda x: int(x), input().split()))
for _ in range(M):
  ans = []
  for i in range(len(A)):
    A[i] += i+1
    if A[i] >= 0:
      ans.append(A[i])
  ans.sort()
  if ans[0] > 0:
    print(0)
  else:
    for i in range(10**9):
      if not i in ans:
        answer = i
        break