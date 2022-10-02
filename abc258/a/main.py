K = int(input())
h = K//60
m = K%60
hh = str(21 + h)
mm = '0'+str(m) if (m < 10) else str(m)
print("{}:{}".format(hh,mm))

