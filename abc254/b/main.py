N = int(input())
for i in range(1, N+1):
  ans = []
  for j in range(1,i+1):
    if j==1 or j ==i:
      ans.append(1)
    else:
      ans.append(tmp[j-2]+tmp[j-1])
  tmp = ans.copy()
  print(*ans)
