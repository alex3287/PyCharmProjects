n = int(input())
k=0
while n % 7 == 0:
    k = k + n // 7
    n = n // 7
if n <= 7:
    print(k)
else:
    print('Не существует')


