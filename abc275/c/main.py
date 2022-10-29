S = [list(input()) for _ in range(9)]
ans_list = []
for i in range(9):
  for j in range(9):
    if (S[i][j]=='#'):
      ans = [i,j]
      ans_list.append(ans)
print(ans_list)
# leng = []
# def f(c,d,x,y):
#   e = c+y
#   f = d-x
# for i in range(len(ans_list)-1):
#   x = ans_list[i][0]-ans_list[i+1][0]
#   y = ans_list[i][1]-ans_list[i+1][1]
#   for j in range(i+1,len(ans_list)):
#     f(ans_list[j][0],ans_list[j][1],x,y)
# print(leng)