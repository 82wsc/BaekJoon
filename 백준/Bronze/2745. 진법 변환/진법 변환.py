import sys

N,B = map(str, sys.stdin.readline().split())

B=int(B)

n=[]

for i in N:
  if i.isdigit() is True:
    n.append(int(i))
  else:
    n.append(ord(i)-55)

n=n[::-1]

r=0
for i in range(len(N)):
  r+=n[i]*(B**(i))
 
print(r)