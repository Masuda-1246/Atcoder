S = list(input())
num = S[1:-1]
if not len(S) == 8:
  print("No")
  exit()
if S[0].isdecimal():
  print("No")
  exit()
elif S[-1].isdecimal():
  print("No")
  exit()
elif S[1]=="0":
  print("No")
  exit()
else:
  for i in range(len(num)):
    if not num[i].isdecimal():
      print("No")
      exit()
  print("Yes")