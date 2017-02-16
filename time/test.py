from timer import Timer

with Timer() as t:
    s=1
    b=10000
    for i in range(1,b+1):
        s*=i
    
print ("=> elasped lpush: %s s" % t.secs)

