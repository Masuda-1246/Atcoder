N = int(input())
W = [input() for _ in range(N)]
last_w = "0"
w_list = []
for w in W:
  for w1 in w_list:
    if last_w != w[0] or w == w1:
      print("No")
      quit()
  last_w = w[-1]
  w_list.append(w)
print("Yes")
  