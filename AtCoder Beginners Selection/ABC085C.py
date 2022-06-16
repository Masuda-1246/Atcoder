n,y = map(lambda x: int(x), input().split())
judge = True
for i in range(n+1):
  for j in range(n-i+1):
    if(10000*i+5000*j+1000*(n-i-j)==y and judge):
      judge = False
      print("{} {} {}".format(i,j,(n-i-j)))
      
if judge:
  print("-1 -1 -1")