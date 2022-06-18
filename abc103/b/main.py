s,t = input(),input()
flag = False
for i in range(len(s)):
  if s==t:
    flag=True
  s=s[-1]+s[:-1]
print("Yes" if (flag) else "No")