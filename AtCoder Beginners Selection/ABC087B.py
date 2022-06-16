A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0
for h in range(A+1):
  for i in range(B+1):
    for j in range(C+1):
      if 500*h+100*i+50*j==X:
        count += 1

print("{}".format(count))