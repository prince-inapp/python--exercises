# ABC Enterprises
import re
import random



global products
products = dict()


class Utils:
    @staticmethod
    def getTaxAmount(price,tax):
        return price * (tax /100)
    
    @staticmethod
    def getDiscountAmt(price, dis):
        return price * (dis/100)

class Product:
    def __init__(self):
        self.__name = ''
        self.__category = ''
        self.product_code = ''
        self.__base_price = 0
        self.__tax = 0
        self.__tax_amount = 0
        self.__mrp = 0
        self.__discount = 0
        self.__discount_amt = 0 #Utils.getDiscountAmt(self.mrp, self.discount)
        self.selling_price = 0 #self.mrp - self.discount_amt
  
    
    def set_selling_price(self):
        s_price = self.__mrp - self.__discount_amt
        self.selling_price = s_price

    
    @property
    def discount_amt(self):
        return self.__discount_amt
    @discount_amt.setter
    def discount_amt(self, amount):
        if(isinstance(amount, (int, float))):
            self.__discount_amt = amount
        else:
            print("enter a valid number")

    @property
    def discount(self):
        return self.__discount
    
    @discount.setter
    def discount(self, dis):
        if(isinstance(dis,(int,float)) and dis>=0 and dis <= 100):
            self.__discount = dis
        else:
            print("enter a valid number")

    @property
    def mrp(self):
        return self.__mrp
    
    @mrp.setter
    def mrp(self, price):
        if(isinstance(price,(int, float))):
            self.__mrp = price
        else:
            print("Enter a valid number")


    @property
    def tax_amount(self):
        return self.__tax_amount
    
    @tax_amount.setter
    def tax_amount(self, amount):
        try:
            x = float(amount)
            self.__tax_amount = x
        except Exception as e:
            print("Enter a valid number. ",type(e.__name__)," Error")
    
    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self, category):
        category = category.upper()
        category_name = { 'HYGIENE', 'HEALTH', 'STAPLES', 'SPORTS', 'FASHION'}
        if(category in category_name):
            self.__category = category
        else:
            print("Enter a valid category")

    @property
    def tax(self):
        return self.__tax
    @tax.setter
    def tax(self, tax):
        if(tax>=0):
            self.__tax = tax
        else:
            print("Enter a valid tax percentage.")
        
    @property
    def base_price(self):
        return self.__base_price
    @base_price.setter
    def base_price(self, base_price):
        if(isinstance(base_price, (int, float))):
            self.base_price = base_price
        else:
            print("Enter a valid price")

    @property #getter
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        if(name.isalpha() and len(name)>=3):
            self.__name = name.upper()
            
        else:
            raise Exception("Name should contain only characters and minimum 3 character long")

    def generateProductCode(self):
        exp = self.__category[0:2] + self.__name[0:2]
        list_of_items = re.findall(exp,str(products.keys()))
        print(list_of_items)
        print(len(list_of_items))
        count = str(len(list_of_items))
        random_numbers = str(random.randint(100,999))
        code = exp + count + random_numbers
        code = code[0:8]
        if(code in products.keys()):
            return self.generateProductCode(self.category,self.name)
        else:
            return code




def displayOptions():
    print('''
    1: Enter a product
    2: Display details particular product
    3: Edit Product details
    4: Manufactuere Calculations
    5: Exit
    ''')


while(True):
    displayOptions()
    opt = int(input("Enter Option"))
    if(opt==1):
        try:
            pro = Product()
            name = input("Enter Name of Product: ")
            pro.name = name.upper()
            cat = input("Enter Category")
            pro.category = cat
            print(pro.category)
            pro.product_code = pro.generateProductCode()
            
            choice_mrp_tax = int(input("""
            1. MRP
              or
            2. Base Price without Tax 
            """))
            if(choice_mrp_tax==1):
                price = float(input("Enter MRP Price: "))
                pro.mrp = price
            elif(choice_mrp_tax==2):
                base_price = float(input("Enter base price"))
                pro.base_price = base_price
            else:
                raise Exception
            choice_tax_percent = int(input("""
            Do you wish to enter 
            1. Tax Percentage
            2. Tax Amount
            choose option
            """))
            if(choice_tax_percent==1):
                taxP = float(input("Enter tax percentage: "))
                pro.tax = taxP
                if(choice_mrp_tax ==2 ):
                    pro.tax_amount = Utils.getTaxAmount(pro.base_price,taxP)
                elif(choice_mrp_tax == 1):
                    temp = pro.mrp * taxP/100
                    pro.tax_amount = temp
            elif(choice_tax_percent == 2):
                tax_amt = float(input("Enter tax amount"))
                pro.tax_amount = tax_amt
                # call function to convert to tax percentage
                temp = pro.mrp - pro.tax_amount
                per = pro.tax_amount * 100 // pro.mrp
                pro.tax = per
            else:
                raise Exception("Enter a valid Choice")
            choice_dis = int(input("""
            Do you wish to enter 
            1. Discount Percentage
            2. Discount Amount
            choose option
            """))
            if(choice_dis==1):
                pro.discount = float(input("enter discount percentage: "))
                pro.discount_amt = pro.mrp * pro.discount
            elif(choice_dis == 2):
                pro.discount_amt = float(input("Enter discount amount: "))
                temp = pro.mrp - pro.discount_amt
                per = pro.discount_amt * 100 // pro.mrp
                pro.discount = per
            products[pro.product_code] = pro
            print(products)
            pro.selling_price = pro.set_selling_price()
            pro.base_price = pro.mrp - pro.tax_amount
        except Exception as e:
            print(type(e).__name__)
            print(e)
    if(opt==2): # display details of particular product
        pro_id = input("enter id of product")
        if pro_id in products.keys():
            obj = products[pro_id]
            print("""
            Name : {}
            Category : {}
            Product Code : {}
            Base Price : {}
            Tax : {} %
            Tax Amount : {} 
            Discount : {}%
            Discount Amount : {}
            MRP : {} 
            Selling Price : {}
            """.format(obj.name,obj.category, obj.product_code, obj.base_price, obj.tax, obj.tax_amount, obj.discount, obj.discount_amt, obj.mrp, obj.selling_price ))
        else:
            print("Product not found...")  

    elif(opt == 3):
        pro_id = input("enter id of product")
    elif(opt == 4):
        pass
    elif(opt==5):
        exit(1)
    
         

    
            
            
