while True:
  n = int(input())
  if n==-1:
    break
  m = [i for i in range(1,n) if n%i==0]
  if sum(m)==n:
    print("%d = "%n,end='') 
    print(*m,sep=' + ')
  else:
    print("%d is NOT perfect."%n)