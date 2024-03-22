N,B = map(int,input().split())

r = []

while N!= 0:
  r.append(int(N%B))
  N = int(N//B)

r=r[::-1]
  
for i in range(len(r)):
  if r[i]>9:
    r[i] = chr(r[i] + 55)
print(*r, sep='')