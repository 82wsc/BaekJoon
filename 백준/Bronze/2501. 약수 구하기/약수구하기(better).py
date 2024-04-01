n,k = map(int,input().split())

m=[i for i in range(1,n+1) if n%i==0]

print(m[k-1] if len(m)>=k else 0)
