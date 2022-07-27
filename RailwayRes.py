import pyodbc
connString = 'Driver={SQL Server};Server=LAPTOP-85QRUTE7\SQLEXPRESS;Database=PhoneBook;Truseted_Connection=yes;'

try:
    conn = pyodbc.connect(connString)
    print("Connected to db")
except Exception as e:
    print(e)
    print("Not connected to db")

class InputValidator:
    def getInt(msg, min, max):
        while True:
            try:
                num = int(input(msg))
                if num < min or num > max:
                    print("Invalid Input... Try again...\n :")
                    continue
                return num
            except Exception as e:
                print("Invalid Input... Try again...\n :")
                continue

class Passenger:
    def __init__(self):
        self.__name = None
        self.trainID = None
        self.seatNumber = None
        self.destination = None
        self.source = None
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

class System:
    def from_and_to(self):
        dest_dict = {'Trivandrum':['Erakulam','Kozhikode'], 
                        'Erakulam':['Kozhikode']}
        print("""From :
        1. Trivandrum
        2. Ernakulam
        3. Kozhikode
        """)
        opt = InputValidator.getInt("Enter your choice : ", 1, 3)
        from_ = dest_dict[list(dest_dict.keys())[opt-1]]
        to = In
        return from_, to