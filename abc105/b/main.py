N = int(input())
for i in range(N//7+1):
  for j in range(N//4+1):
    if (j*4+i*7==N):
      print("Yes")
      quit()
print("No")