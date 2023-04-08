N = int(input())
S = list(input())
x,y = 0,0
point = ["0_0"]
for s in S:
  if s == "R":
    x+=1
  if s == "L":
    x-=1
  if s == "U":
    y+=1
  if s == "D":
    y-=1
  point.append(f'{x}_{y}')

point_set = list(set(point))

print("Yes" if len(point) != len(point_set) else "No")