X, Y, Z=map(int,input().split())
if 0 < Y < X:
  print((abs(Z) + abs(Z - X)) if Z < Y else -1)
elif X < Y < 0:
  print((abs(Z) + abs(Z - X)) if Z > Y else -1)
else:
  print(abs(X))