N = int(input())
XY = [list(map(int, input().split())) for _ in range(int(N))]
XY = sorted(XY, key=lambda x:x[0])

def a(XY):
  for i in range(len(XY)-1):
    if (XY[i][1] >= XY[i+1][0]):
      XY[i][1] = XY[i+1][1]
      XY.pop(i+1)
      break
  return XY

for i in range(len(XY)):
  last = XY.copy()
  XY = a(XY)
  if last == XY:break

for x,y in XY:
  print("{} {}".format(x,y))



