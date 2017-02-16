from random import choice, randint

n=int(input("Введите размер массива\t"))
B = [randint(-20,20) for i in range(n)]

def three(A):
    """Деления списка на три части"""
    t=choice(A)
    A1 = [i for i in A if i < t]
    A2 = [i for i in A if i == t]
    A3 = [i for i in A if i > t]
    return A1, A2, A3

def quik(A):
    if len(A) <2: return A
    W, E, R = three(A)
    return quik(W) + E + quik(R)

print(quik(B))
