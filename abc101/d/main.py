k = int(input())
x = y = 1
for i in range(k):
  print(x)
  num = x + y
  if y * sum(map(int,f'{num}')) < num:
    y *= 10
    x += y
  else:
    x = num