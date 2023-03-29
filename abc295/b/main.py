R, C = map(int, input().split())

B = [input() for _ in range(R)]
for i in range(R):
  for j in range(C):
    x = B[i][j]
    for i2 in range(R):
      for j2 in range(C):
        x2 = int(B[i2][j2]) if B[i2][j2].isdigit() else - 1
        if abs(i-i2) + abs(j-j2) <= x2:
          x = "."
    print(x, end="")
  print()
