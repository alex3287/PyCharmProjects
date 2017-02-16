n = int(input())
sum = 0
while n > 0:
    digit = n % 10
    if digit < 7:
        sum += 1
    n = n // 10
print(digit)

dfg
