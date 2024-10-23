# Dictionary in python 
# len()
d = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(len(d)) # output 3 

# clear()

d1 = {
    'name': "Shivam",
    "age": 20,
    "roll": "SDE"
}
print(d.clear()) # output {}

# copy()

d2 = {
    "Name":"Shbham",
    "age": 18
}
print(d.copy()) # output { 'name':"Shubham", 'age': 18 }

# fromkeys(s,[,value])
keys = ['x','y','z']
new_dict = dict.fromkeys(keys, 0)
print(new_dict)

# get(k,[,v])
d3 = { 'a':1,'b':2 }
print(d3.get('a'))
print(d.get('c',"Not Found."))

#items()
print(d3.items())

# keys()
print(d3.keys())

#pop([,deafult])
print(d3.pop())

print(d3.popitem())

# setdeafult(k [,v])
 