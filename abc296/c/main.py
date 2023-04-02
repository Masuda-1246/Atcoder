N, X = map(int, input().split())
A = set(list(map(int, input().split())))

for a in A:
  aj = a - X
  if aj in A:
    print("Yes")
    exit()
print("No")