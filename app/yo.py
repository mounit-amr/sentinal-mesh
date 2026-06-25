# class vehicle:
#     def __init__(self, type): 
#         self.type = type

# carone = vehicle('fourwheeler')

# print(carone.type)
        
class name:
    def __init__(self, name):
        self.name = name
        
    def curse(self):
        print("yo heres my nga", self.name)
        
n1 = name('MOUNIT')
n2 = name('King VOn')

# n1.curse()

# name.curse(n1)

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def details(self):
        print("name:", self.name)
        print("age:", self.age)
        
s_one = student('Rahul', '19')

# student.details(s_one)

s_one.details()