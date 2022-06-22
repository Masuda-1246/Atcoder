H, W = map(int,input().split())
A = [list(input()) for _ in range (H)]
A_copy = []
for h in zip(*A):
  if "#" in list(h):
    A_copy.append(list(h))
answer = []
for w in zip(*A_copy):
  if "#" in list(w):
    answer.append(list(w))
for ans in answer:
  print(*ans,sep="")
  
# 模範
# H, W = map(int, input().split())
# HW = [list(input()) for _ in range(H)]
# tmp = []
# for h in HW:
#     if h.count("#") == 0:
#         continue
#     tmp.append(h)
# HW = tmp.copy()
# tmp = []
# for w in zip(*HW):
#     if w.count("#") == 0:
#         continue
#     tmp.append(list(w))
# for ans in tmp:
#     print(*ans,sep="")