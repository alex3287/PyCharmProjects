m, n = map(int, input().split())
k=1
t=1
while k*k*k <= n:
    if k*k*k > m:
        t += 1
    k += 1
print(t)

