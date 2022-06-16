n = input()
a = list(map(lambda x: int(x), input().split()))
a.sort(reverse=True)
Alice = 0
Bob = 0
for i in range (int(n)):
  if i%2==0:
    Alice += a[i]
  else:
    Bob += a[i]

print(Alice-Bob)
