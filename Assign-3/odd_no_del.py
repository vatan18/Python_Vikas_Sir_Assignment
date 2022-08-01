#deletes all odd numbers
def del_odd(*args):
    if len(args)==0:
        return -1
    return [num for num in args if num % 2 == 0]#list comprehension
result=del_odd(1,2,3,4,5,6,7,8,9)
print(result)

def dele_odd(list):
    return [num for num in list if num % 2 == 0]#list comprehension
print(dele_odd([34,2,45,9,213,999]))