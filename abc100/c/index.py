def devideCount(x):
  cnt = 0
  while (x%2==0):
    cnt+=1
    x /= 2
  return cnt

n = input()
a = list(map(int, input().split()))
a2 = list(map(lambda x: devideCount(x),a))
print(sum(a2))
    

