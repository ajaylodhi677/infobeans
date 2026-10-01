class Student:
    def __init__(self,roll,name,salary):
        self.__roll=roll
        self.__name=name
        self.__salary=salary
    @property
    def roll(self):
        return self.__roll 
    @property
    def name(self):
        return self.__name 
    @property
    def salary(self):
        return self.__salary   
    @name.setter
    def name(self,name):
        self.__name=name  
    @salary.setter
    def name(self,salary):
        self.__salary=salary
    @name.deleter
    def name(self):
        del self.__name 
    @name.deleter
    def salary(self):
        del self.__salary 
s1=Student(101,"ajay",40000)
print(s1.roll)    
print(s1.name)
print(s1.salary)                        
