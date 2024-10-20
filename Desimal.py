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