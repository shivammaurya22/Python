""" Functions that take other functions as arguments, or that return functions, are called higher order functions. Python 3 contains two built-in higher order functions, filter() and map(). Note that in earlier versions of Python, these functions returned lists; in Python 3, they return an iterator, making them much more efficient """

lst = [1,2,3,4,5]
lst = list(map(lambda x: x**3, lst))
print(lst)
# Similiar with Filter() in python 
lst = list(filter(lambda x: x > 25, lst))
print(lst)

words = "The GoD is back, as Shivam Maurya!"
words = str.split(words)
words = sorted(words, key=len)
print(words)

def iterTest(low,high):
    while low <= high:
        print(low)
        low += 1
        
def recurTest(low,high):
    if low <= high:
        print(low)
        recurTest(low+1,high)
  
print(iterTest(2,4))
print(recurTest(2,4)) 

def oddGen(n,m):
    while n < m:
        yield n
        n +=  2
 
print(oddGen(2,4))               