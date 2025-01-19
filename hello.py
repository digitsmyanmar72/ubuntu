class myclass():
    def __init__(self,name,age):
         self.name = name
         self.age = age
    def func(self):
         print(self.name,self.age)

obj = myclass("nay",42)

print(obj.name)
obj.func()

        