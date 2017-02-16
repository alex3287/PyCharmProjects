def simple2(n):
    n1=n+1
    P=set(range(1,n1))
    for i in range(2, int(n1**0.5)+1):
        if i in P:
            P -= set(range(i*i,n1,i))
    return P
if __name__=='__main__':

    m2 = int(input('Enter max number >>>'))
    print(simple2(m2))