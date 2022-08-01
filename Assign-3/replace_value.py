def replace(l, to, by):
   return [by if item == to else item for item in l]
L =[ "abc", "def", "abc" ]
result = replace(L, "abc", "xyz")
print(result)