import time
start = time.time()
s=0
for i in range(10000,8000000):
    s+=i
print(s)
end = time.time()
t = end - start
print(round(t,2))