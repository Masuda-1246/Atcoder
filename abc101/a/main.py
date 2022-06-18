ss = list(input())
ans = 0
for s in ss:
  ans += 1 if(s=="+") else -1
print(ans)