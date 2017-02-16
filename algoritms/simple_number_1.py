m1=int(input('Enter min number >>>'))
m2=int(input('Enter max number >>>'))
n=m2+1
A=[True]*n

for i in range(2,int(n**0.5)+1):
    if A[i]:
        for j in range(i*i,n,i):
            A[j]=False

for k in range(m1,n):
    if A[k]:
        print(k,end=' ')



