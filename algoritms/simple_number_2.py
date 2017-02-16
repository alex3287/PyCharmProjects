def simple(m1,m2):
    '''
    выборка простых чисел в указанном
    диапозоне
    '''
    n = m2 + 1
    A = [True] * n

    for i in range(2, int(n ** 0.5) + 1):
        if A[i]:
            for j in range(i * i, n, i):
                A[j] = False

    for k in range(m1, n):
        if A[k]:
            print(k, end=' ')

if __name__=='__main__':
    m1 = int(input('Enter min number >>>'))
    m2 = int(input('Enter max number >>>'))
    simple(m1,m2)