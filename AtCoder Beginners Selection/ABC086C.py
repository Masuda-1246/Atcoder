n = input()
datas = [list(map(int,input().split())) for _ in range(int(n))]
t_pre = x_pre = y_pre = 0
f = True

for data in datas:
  dist = abs(data[1]-x_pre) + abs(data[2]-y_pre)
  time = data[0] - t_pre
  t_pre, x_pre, y_pre = data
  
  if time < dist:
    f = False
  elif time%2 != dist%2:
    f = False
    
print("Yes" if(f) else "No")