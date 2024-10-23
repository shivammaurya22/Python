# namedtuple()

from collections import namedtuple

Point = namedtuple('Point',['x','y'])
# create a instance of the Point 
p = Point(10,20)

print(p.x) # output 10
print(p.y) # output 20

# deque in python 
from collections import deque
# create a deque 
d = deque([1,2,3])

# Append to the right and left 
d.append(4)
print(d)
d.appendleft(0)
print(d)

# pop from the right and left 
d.pop()
print(d)
d.popleft()
print(d)

# ChainMap
from collections import ChainMap
# create two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c':4}

# create a ChainMap
cm = ChainMap(dict1,dict2)

print(cm['a'])
print(cm['b'])
print(cm['c'])

# Another example of the chainMap
defaults = {'theme': 'Default', 'language': 'eng', 'showIndex': True, 'showFooter': True}
cm1 = ChainMap(defaults)
cm2 = cm1.new_child({'theme': 'bluesky'})
print("the value of the cm2 theme:-",cm2['theme'])
print("Pure cm2 variable:-",cm2)
print("Operation Pop the element:-",cm2.pop('theme'))
print("After pop the element:-",cm2['theme'])
cm2.maps[0] = {'theme':'desert', 'showIndex':False }
print("The value of the showIndex of cm2:-",cm2['showIndex'])

# counter in python 
from collections import Counter
# create a counter
count = Counter([1,2,3,4,2,3,4,2,4,2,3])
print(count)

# orderedDict 
from collections import OrderedDict
# create a OrderedDict 
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)

