# Using if else
x=int(input("Enter first number: "))
y=int(input("Enter 2nd number: "))
if x>y:
    print(f"maximum no is = {x}")
else:
    print(f"maximum no is = {y}")

# Using Turnary operator
x=int(input("Enter first number: "))
y=int(input("Enter 2nd number: "))
print(f"maximum no is = {x if x>= y else y} ")

# Using max function
def check(x,y):
   return max(x,y)  
x=8
y=9
print(f"maximum no is {check(x,y)}")