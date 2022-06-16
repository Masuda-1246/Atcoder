n,a,b = (map(lambda x: int(x), input().split()))
cnt = 0
for i in range(1,(n+1)):
  str_i = str(i)
  ans = 0
  for j in range (len(str_i)):
    ans += int(str_i[j])
  if (a<=ans | ans<=b):
    cnt += i
    
print(cnt)