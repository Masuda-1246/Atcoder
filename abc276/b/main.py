N, M = map(lambda x: int(x), input().split())
AB = [list(map(lambda x: int(x), input().split()))for _ in range(M)]
dic = {i:[] for i in range(1,N+1)}

for ab in AB:
  dic[ab[0]].append(ab[1])
  dic[ab[1]].append(ab[0])
for i in range(1,N+1):
  dic[i] = sorted(list(set(dic[i])))
for i in range(1, N+1):
  print(len(dic[i]), *dic[i])
