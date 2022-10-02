N, X = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(int(N))]
AB_sum = []
d = 0
for a, b in AB:
  AB_sum.append(a+b*X+d)
  d += a + b
  X -= 1
  if X == 0:
    break
print(min(AB_sum))
