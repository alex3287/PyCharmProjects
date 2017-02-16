
def simple3(m1,m2):
    n=m2+1
    for i in range(m1,n):
        for j in range(2, int(i**0.5)+1):
            if i % j ==0:
                break
        else:
            print(i, end=' ')

if __name__=='__main__':
    #m1 = int(input('Enter min number >>>'))
    #m2 = int(input('Enter max number >>>'))
    simple3(100000,1000000)