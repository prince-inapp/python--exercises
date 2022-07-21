class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        print("Sum : ",self.num1 + self.num2)
    
    def multiply(self):
        print("Product :",self.num1 * self.num2)
    
    def divide(self):
        print("Division :", self.num1 / self.num2)
    
    def subtract(self):
        print("Difference :", self.num1 - self.num2)

obj = calculator(2,3)
obj.add()
obj.multiply()
obj.divide()+