import time

def oddGen(n,m):
    while n < m:
        yield n
        n += 2

def oddLst(n,m):
    lst = []
    while n < m:
        lst.append(n)
        n += 2
    return lst 
t1 = time.time()
print(sum(oddGen(1,100000)))
print("Time to Sum an Iterator: %f" %(time.time()- t1))

t1 = time.time()
print(sum(oddLst(1,100000)))
print("Time to build and sum a list: %f" % (time.time() - t1 ))