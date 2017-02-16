f1 = open('input.txt')
f2 = open('output.txt','w')
n = int(f1.readline().rstrip())
s = f1.readline().rstrip().split()
mas = [int(i) for i in s]
for i in range(n):
    if i%2==0:
        f2.write(str(mas[i])+' ')
f1.close()
f2.close()

