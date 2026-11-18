from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def intrest(self):
        print("Bank intrest")
class Sbi(Bank):
    def intrest(self):
        print("Sbi interset ")
class hdfc(Bank):
    def intrest(self):
        print("Hdfc intrest")
#obj=Bank()  error
obj1=Sbi()
obj1.intrest()
obj2=hdfc()
obj2.intrest() 
Bank.intrest(obj1)                  