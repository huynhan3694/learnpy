c = {'a': 10, 'b': 33, 'c': 20, 'd': 13}
tmp = list();
for k ,v in c.items():
    tmp.append( (v,k) )
print(tmp)
# Sap xep trong python
tmp = sorted(tmp, reverse=True)
print(tmp)