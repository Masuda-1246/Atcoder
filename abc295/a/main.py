N = int(input())
Ws = input().split()

for i in range(N):
  if Ws[i] == "and":
    print("Yes")
    quit()
  elif Ws[i] == "not":
    print("Yes")
    quit()
  elif Ws[i] == "that":
    print("Yes")
    quit()
  elif Ws[i] == "the":
    print("Yes")
    quit()
  elif Ws[i] == "you":
    print("Yes")
    quit()
print("No")