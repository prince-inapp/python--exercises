import functools
import pyodbc
from abc import ABC, abstractmethod

server_one = 'DESKTOP-CKLRF1B\SQLEXPRESS'
server_two = 'LAPTOP-85QRUTE7\SQLEXPRESS'
server_ = server_one
connString = 'Driver={SQL Server};Server={'+server_+'};Database=RailwayReservation;Truseted_Connection=yes;'
#print(connString)
def dbms(func):
    @functools.wraps(func)
    def innerWrapper(*args):
        try:
            conn = pyodbc.connect(connString)
        except:
            print('Connection Error')
            return None
        else:
            curr = conn.cursor()
            value = func(curr, *args)
            conn.commit()
            conn.close()
            return value
    return innerWrapper

@dbms
def getStations(cur):
    try:
        cur.execute('SELECT * FROM Stations;')
        stations = {}
        for id, station_name in cur:
            stations[station_name] = id
        return stations
    except Exception as e:
        print(e)
@dbms
def getTrainID(cur, dest):
    try:
        cur.execute('select * from Trains;')
        for train_id, train_name, destination, booked_seats, waiting_list in cur:
            if int(destination) >= dest:
                if(booked_seats<5):
                    print(train_name)
                    return train_id
        return False
    except Exception as e:
        print("Error: ",e)

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
    
    def getInt(msg, min, max):
        while True:
            try:
                opt = int(input(msg))
                if(opt>=min and opt <= max):
                    return opt
                else:
                    raise Exception("Out of range")
            except Exception as e:
                print("Enter a valid number...")
                continue

class Passenger:
    def __init__(self):
        self.__name = None
        self.trainID = None
        self.seatNumber = None
        self.destination = None
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

'''
class Train:

    def __init__(self, trainID,trainName,destination):
        #self.source = source
        self.destination = destination
        #self.stops = stops
        self.trainID = trainID
        self.trainName = trainName
        self.noOfSeats = 5
        self.seats = {} #{seatNumber: Passenger}
        self.passengers = [] # list of passengers
'''

class System:

    stations = getStations()
    # trains

    def enterPassengerDetails(self):
        name = input("Enter Name: ")
        passenger = Passenger()
        passenger.name = name
        return passenger

    def getDest(self):
        #stations = {1: 'TVM', 2: 'ALP', 3: 'ERN', 4: 'KZK'}
        stops = {'TVM': ['ALP', 'ERN', 'KZK'],
                 'ALP': ['ERN', 'KZK'],
                 'ERN': ['KZK']}
        print("""Please enter your destination: 
        ALP
        ERN
        KZK""")
        #from_ = InputValidator.getCheckString("Enter Source Station: ", self.stations.values())
        #temp = "\n\t\t".join(stops[from_])
        #print(temp)
        #print("TO:"+"\n\t\t"+temp+"\n")
        dest = InputValidator.getCheckString("Enter Destination Station: ", self.stations.keys())
        
    
    def bookTrain(passenger):
        train_details = getTrainID(passenger)

system = System()
while True:
    print('''
    1. Book a ticket
    2. List all passengers
    3. List Waiting List Passengers
    4. Exit
    ''')
    opt = InputValidator.getInt("Choose Option : ", 1,4)
    if(opt==1):
        passenger = system.enterPassengerDetails()
        passenger.destination = system.getDest()
        passenger.trainID = getTrainID(passenger.destination)
        

