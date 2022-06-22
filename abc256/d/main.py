N = int(input())
XY = [list(map(int, input().split())) for _ in range(int(N))]
XY = sorted(XY, key=lambda x:x[0])
ans = []
ans.append(XY[0])
for i in range(1,len(XY)):
  if (XY[i][0] <= ans[-1][1]):
    ans[-1][1] = XY[i][1]
  else:
    ans.append(XY[i])
for x,y in ans:
  print("{} {}".format(x,y))
