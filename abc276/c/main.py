N = int(input())
P = list(map(lambda x: int(x), input().split()))
max_num = 0
max_index = 0
for i in range(len(P)):
  if (P[i] > max_num):
    max_num = P[i]
    max_index = i
P_pre = P[:max_index+1]
P_rea = P[max_index+1:]
print(P_pre,P_rea)