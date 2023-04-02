N, Q = map(int, input().split())
call = 1
called = set()
ans = 1
for q in range(Q):
    event= input().split()
    if event[0] == "1":
        called.add(call)
        call+=1
    elif event[0] == "3":
        while ans not in called:
            ans+=1
        print(ans)
    else:
        called.remove(int(event[1]))