from abc import ABC, abstractmethod

class calculator(ABC):
    
    __num1 = None
    __num2 = None
    
    @property
    def num1(self):
        return self.__num1
    @num1.setter
    def num1(self, number):
        try:
            number = int(number)
            self.__num1 = number
        except:
            print("Invalid Number")
    
    @property
    def num2(self):
        return self.__num2
    @num2.setter
    def num2(self, number):
        try:
            number = int(number)
            self.__num1 = number
        except:
            print("Invalid Number")

    @abstractmethod
    def calculate(self):
        pass

class CalcSum(calculator):
    def calculate(self):
        return self.num1 + self.num2

class CalcDiff(calculator):
    def calculate(self):
        return self.num1 - self.num2

class CalcProd(calculator):
    def calculate(self):
        return self.num1 * self.num2

class CalcQuo(calculator):
    def calculate(self):
        try:
            return self.num2 / self.num1
        except:
            return ": Error Denominator can't be 0"

calculator.num1 = 10
calculator.num2 = 5

sum = CalcSum()
diff = CalcDiff()
prod = CalcProd()
quo = CalcQuo()

print("Sum",sum.calculate())
print("Difference",diff.calculate())
print("Quotient", quo.calculate())
print("Product",prod.calculate())
