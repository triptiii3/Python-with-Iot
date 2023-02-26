#OOPs
# class person:
#     def fun():
#         print("this is fun")
# obj=person()
# person.fun()

# #init method or constructor
# # def __init__(self,name):
# #     self.name=name

# #sample method
# def say_hi(self):
#     print("my name is",self.name)

# obj=person()
# obj.say_hi() #=> this gives no attribute error
#if in init self,name="" and no name passed in obj.persin then it will give no value but the funct will run

# class Employee:
#     empCount = 0
#     def __init__(self,name,salary) :
#         self.name=name
#         self.salary=salary
#         Employee.empCount+=1

#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount) 

#     def displayEmployee(self):
#         print("Name : ",self.name, ",Salary: ", self.salary)
    
#     def get_details(self,name):
#         print("User details:",self.name,self.exp)

# obj1=Employee('anuj','delhi','10')
# obj2=Employee('gaurav','Noida','20')
# obj3=Employee('mahesh','ggn')

# obj1.get_details('anuj')
# obj2.displayCount()

#CLASS INHERITANCE

class Parent: #define parent class
    __parentAttr=100
    def __new__(self): 
        print("new funct has been called")
        return super(Parent,self).__new__(self)
    def __init__(self):
        print("Calling parent constructor")
    def parentMethod(self):
        print("Calling parent method")
    def setAttr(self,attr):
        Parent.__parentAttr=attr
    def getAttr(self):
        print("Parent attribute:",Parent.__parentAttr)
class child(Parent): #define child class
    def __init__(self):
        print("Calling child constructor")
    def childMethod(self):
        print('calling child method')
c=child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

print(c._Parent__parentAttr)