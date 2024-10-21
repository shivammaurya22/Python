import decimal

x = decimal.Decimal(3.14); y = decimal.Decimal(2.74)

print(x * y)

decimal.getcontext().prec = 4
print(x * y)

import fractions

print(fractions.Fraction(3,4))
print(fractions.Fraction(0.5))
print(fractions.Fraction(".25"))

d = {
    'one' : 1,
    'two' : 2, 
    'three' : 3
}

d['four'] = 4
d.update({
    'five' : 5,
    'six' : 6
})
print(d)
print('five' in d)
print(sorted(list(d.values())))
print(sorted(list(d), key=d.__getitem__))
print([value for (key, value) in sorted(d.items())])
print(sorted(list(d), key=d.__getitem__, reverse = True))

d2 = {
    'one' : 'Shivans',
    'two' : 'Shivam',
    'three' : 'chinnu',
    'four' : 'India',
    'five' : 'Sandhya'
}

print(sorted(d2, key=d.__getitem__))
print([d2[i] for i in sorted(d2, key=d2.__getitem__)])

def corder(string):
    return(string[len(string) - 1])

print(sorted(d2.values(), key=corder))

def wordcount(fname):
    try: 
        fhand = open(fname)
    except:
        print('File cannot be opened.')
        exit()
    count = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
        return(count)    
    
count = wordcount('./alice.txt')
filtered = { key:value for key, value in count.items() if value < 20 and value > 15 }    
print(filtered)                    