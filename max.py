# Return the maxmimum of list
def maximum(arr):
    big = arr[0]
    for ele in arr:
        if(ele > big):
           big = ele
    return big 

list1 = [1,2,5,2,6]
result =maximum(list1)
print(result)