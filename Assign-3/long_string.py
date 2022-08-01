#longest string
def long_string(*args):
    if len(args)==0:
        return -1
    lenth=-1
    for ele in args:
        if len(ele)>lenth:
            lenth=len(ele)
    return ele
result=long_string("jai","Viru","biswajeet")
print(result)
#or
#longest string
def long_string(l1):
   length=-1
   for ele in l1:
       if len(ele)>length:
           length=len(ele)
   return ele
print(long_string(["jai","Viru","biswajeet"]))

