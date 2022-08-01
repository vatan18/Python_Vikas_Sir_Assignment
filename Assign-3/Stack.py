class Stack:
   
   def __init__(self):#initializing stack
    self.list=[]

   def push(self, elem):
    self.list.append(elem)#pushing in stack in last
    print(self.list)
   
   def pop(self):
    if(self.list==[]):
        print("stack empty")
    else:
     self.list.pop() #removing from last
     return print(self.list) #returning the updated stack
 

