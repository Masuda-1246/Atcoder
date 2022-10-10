N = input()
odd, even  = [], []
for i in input().split():
  if int(i)%2 == 1:
    even.append(int(i))
  else:
    odd.append(int(i))
odd.sort(), even.sort()
ans = -1
if len(odd)>1 and len(even)>1:
  ans = max(odd[-1]+odd[-2],even[-1]+even[-2])
elif len(odd)>1:
  ans = odd[-1]+odd[-2]
elif len(even)>1:
  ans = even[-1]+even[-2]
print(ans)