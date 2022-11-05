C = list(map(lambda x: int(x), input().split()))
for c in C:
  if c == 1:
    print("L")
  elif c == 2:
    print("B")
  else:
    print("R")