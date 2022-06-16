n = input()
a = list(map(lambda x:int(x),input().split()))

 
count = 0
j = 0
 
while j < 1:
  judge = 0
  for i in range(n):
    if (a[i]%2==0):
      judge += 1
      a[i] = a[i]/2
  if(judge != n):
    j = 1
  else:
    count += 1
 
print(count)