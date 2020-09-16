a = ['a','b','c','d','e','a','a','b','c', 'l']
b = {a[i]:[k for k,v in enumerate(a) if v == a[i]] for i in range(len(a))}
print(b)