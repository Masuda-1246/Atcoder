N = int(input())
XYH = [list(map(int, input().split())) for _ in range(int(N))]

for i in range(N):
  if XYH[i][2] != 0:
    break
for x in range(101):
  for y in range(101):
    H = XYH[i][2] + abs(XYH[i][0]-x)+ abs(XYH[i][1]-y)
    for j in range(N):
      if XYH[j][2] != max((H - abs(XYH[j][0]-x) - abs(XYH[j][1]-y)),0):
        break
    else:
      print(x,y,H)
      
