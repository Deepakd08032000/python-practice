# set = collection of well define object
s = set()
print(type(s))
# set retained unique value.
s.add(1)
s.add(2)
s1 = s.union({1,2,3})
print(s)
print(s1)