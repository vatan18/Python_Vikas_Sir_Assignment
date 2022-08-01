# Return min and max (without looping twice)
def max_min_value(list):
    max = list[0]
    min = list[0]
    for i in list:
        if i > max:
            max = i
        if i< min:
            min=i
    return max,min
num = [1, 6, 5, 3, 2, 7, 9, 5, -9]
minVal, maxVal = max_min_value(num) 
print("min = ", minVal, " max = ", maxVal)