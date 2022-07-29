import pyodbc
from abc import ABC, abstractmethod

server_one = 'DESKTOP-CKLRF1B\SQLEXPRESS'
server_two = 'LAPTOP-85QRUTE7\SQLEXPRESS'
server_ = server_one
connString = 'Driver={SQL Server};Server={'+server_+'};Database=PhoneBook;Truseted_Connection=yes;'
print(connString)
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

class Train(ABC):

    def __init__(self):
        self.source = None
        self.destination = None
        self.stops = []
        self.trainID = None
        self.trainName = None
        self.noOfSeats = 5
        self.seats = {}
        self.passengers = []


class System:
    

    def from_and_to(self):
        dest_dict = {1:['Trivandrum','Alappuzha','Eranakulam', 'Kozhikode'],
                     2:['Eranakulam', 'Kozhikode'],
                     3:['Kozhikode']}
        print("""From :
        1. Trivandrum
        2. Alleppy
        3. Ernakulam
        4. Kozhikode
        """)
        opt = InputValidator.getInt("Enter your choice : ", 1, 3)
        from_ = dest_dict[opt][0]
        to = InputValidator.getInt("Enter Your Choice : ", 1,3)
        return from_, to
        