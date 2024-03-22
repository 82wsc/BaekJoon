N,B = map(int,input().split())

r = []

while N!= 0:
  c = int(N%B)
  r.append(c)
  N = int(N//B)

r=r[::-1]
  
for i in range(len(r)):
  if r[i]>9:
    r[i] = chr(r[i] + 55)
print(*r, sep='')