N = int(input())
S = list(input())
odd = 0
ans = []
for s in S:
  if s=='"':
    odd+=1
  if odd%2==0 and s==',':
    ans.append('.')
  else:
    ans.append(s)
print(*ans, sep='')