a = 7

b = bin(a)
print(b)

c = 25

d = bin(c)
print(d)

# conversion shown with sentence form

print('We have', a, 'in binary form ', b)
print('We have', c, 'in binary form ', d)

# conversion to decimal from binary

e = b
print('e is equal', e)
f = ('We have', e, 'converted to decimal', int(e, 2))
print(f)

# conversion to octal number
g = 10
print('g is equal', g)
h = oct(g)
print(h)

# conversion to decimal from octal

i = h
print('i is equal', i)
# when reconversion, int (variable,data converted into binary/octal/hexadecimal)
j = ('We have', i, 'converted to decimal', int(i, 8))
print(j)

# conversion to hexa-decimal number
k = 13
print('k is equal', k)
l = hex(k)
print(l)

# conversion to decimal from hexa-decimal
m = l
print('m is equal', m)
n = ('We have', m, 'converted to decimal', int(m, 16))
print(n)
