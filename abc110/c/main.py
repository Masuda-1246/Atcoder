S = list(input())
T = list(input())
ds = {chr(ord("a")+i):[] for i in range(26)}
dt = {chr(ord("a")+i):[] for i in range(26)}
for i in range(len(S)):
  ds[S[i]].append(i)
  dt[T[i]].append(i)
print(sorted(list(ds.values())))
print(sorted(list(dt.values())))
print("Yes" if (sorted(list(ds.values())) == sorted(list(dt.values()))) else "No")