R=6
A=[]
MAX=1001
minp=MAX*MAX
ma=MAX
me=MAX
n=int(input('>'))
for i in range(R):
    A.append(int(input('>>')))
for i in range(R,n):
    a_=int(input('>>>'))
    if A[0] < ma:
        ma=A[0]
    if A[0]%2==0 and A[0] < me:
        me=A[0]
    if a_ % 2 ==0:
        p=ma*a_
    elif me < MAX:
        p=me*a_
    else: p = MAX * MAX
    if p < minp:
        minp=p
    for i in range(R-1):
        A[i]=A[i+1]
    A[R-1]=a_
if minp == MAX*MAX:
    mp=-1
print(minp)
