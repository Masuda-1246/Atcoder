K = int(input())
ans = []
for i in range(65, 65+K):
  ans.append(chr(i))
print(*ans, sep='')