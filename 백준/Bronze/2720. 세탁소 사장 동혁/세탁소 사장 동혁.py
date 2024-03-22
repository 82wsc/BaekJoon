T = int(input())
p = [25, 10, 5, 1]
r = []
m=[]
for _ in range(T):
  C = int(input())
  for i in range(len(p)):
    r.append(C // p[i])
    C = C % p[i]
  m.append(r)
  r = []

for i in m:
  print(*i,sep=' ')