import pyodbc
from abc import ABC, abstractmethod

connString = 'Driver={SQL Server};Server=LAPTOP-85QRUTE7\SQLEXPRESS;Database=PhoneBook;Truseted_Connection=yes;'

try:
    conn = pyodbc.connect(connString)
    print("Connected to db")
except Exception as e:
    print(e)
    print("Not connected to db")

class InputValidator:
    @staticmethod
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
    @staticmethod
    def getCheckString(msg, stationList ):
        while True:
            try:
                str = input(msg).upper()
                if str not in stationList:
                    print("Invalid Input... Try again...\n :")
                    continue
                return str
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
        self.stops = None
        self.trainID = None
        self.trainName = None
        self.noOfSeats = 5
        self.seats = {} #{seatNumber: Passenger}
        self.passengers = [] # list of passengers



class System:
    stations = {1: 'TVM', 2: 'ALP', 3: 'ERN', 4: 'KZK'}
    def from_and_to(self):
        #stations = {1: 'TVM', 2: 'ALP', 3: 'ERN', 4: 'KZK'}
        stops = {'TVM': ['ALP', 'ERN', 'KZK'],
                 'ALP': ['ERN', 'KZK'],
                 'ERN': ['KZK']}
        print("""FROM: 
        TVM
        ALP
        ERN
        KZK""")
        from_ = InputValidator.getCheckString("Enter Source Station: ", self.stations.values())
        temp = str(stops[from_]).join('\n')
        print(temp)
        print("""TO:
        {}""".format(temp))
        to_ = InputValidator.getCheckString("Enter Destination Station: ", self.stations.values())
        return from_, to_

p = System().from_and_to()
print(p)