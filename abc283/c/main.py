S = list(input())
cnt = 0
for s in S:
  if s=="0":
    if next_0!=1:
      cnt += 1
      next_0 = 1
    else:
      next_0 = 0
  else:
    cnt+=1
    next_0 = 0
print(cnt)