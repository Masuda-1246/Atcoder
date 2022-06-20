S = list(input())
judge = True
if (S[0]!="A" or S[1]=="C" or S[-1]=="C"):
  judge = False

cnt = 0
for i in range(1,len(S)):
  if (S[i]=="C"):
    cnt+=1
  elif S[i].islower()==False:
    judge = False
    break
  if cnt > 1:
    judge = False
    break
if cnt == 0:
  judge = False
  
print("AC" if judge else "WA")

#模範
a = input()
 
if a[0] == 'A' and ('C' in a[2:-1]) and a[2:-1].count('C') == 1:
    str = a[1:2] + a[3:].replace('C', '')
    if str.islower():
        print('AC')
        quit()
 
print('WA')