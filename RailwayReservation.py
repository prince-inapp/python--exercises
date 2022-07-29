import dbm
import functools
import pyodbc
from abc import ABC, abstractmethod

server_one = 'DESKTOP-CKLRF1B\SQLEXPRESS'
server_two = 'LAPTOP-85QRUTE7\SQLEXPRESS'
server_ = server_one
connString = 'Driver={SQL Server};Server={'+server_+'};Database=RailwayReservation;Truseted_Connection=yes;'
#print(connString)

global passengerID
passengerID = 1

train = {
    101 : 'TVM-ALP',
    102 : 'TVM-ERN',
    103 : 'TVM-KZK'
}

def getTrainId(dest):
    pass


class InputValidator:
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
                    print("Error")
                    raise Exception("Out of range")
            except Exception as e:
                print("Enter a valid number...")
                continue
    

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
        # print([i for i in cur.fetchall()])
        for row in cur.fetchall():
            print(row[2])
            waiting_list= row[4]
            print("Booked seats", row[3])
            if int(row[2]) >= dest:
                if(row[3]<5): #seat
                    print(row[1])
                    print(row[0])
                    return int(row[0])
                else:
                    continue
        return False
    except Exception as e:
        print("Error: ",e)

@dbms
def addToWaitingList(cur):
    cur.execute()

@dbms
def bookTicket(cur,name, dest, trainId):
    cur.execute('INSERT INTO Passengers values (?,?,?) ',(name, dest, trainId))
    cur.execute(f'select booked_seats from Trains where train_id = {trainId}')
    print("Booking Success!")
    seats = [i for i in cur.fetchall()]
    print(seats)
    seat = 0
    seat = seats[0][0] + 1
    print(seat)

    cur.execute('update Trains set booked_seats = ? where train_id = ?',(seat, trainId))
    print("success")
while True:
    print('''
    1. Book a ticket
    2. List all passengers
    3. List Waiting List Passengers
    4. Exit
    ''')
    opt = InputValidator.getInt("Choose Option : ", 1,4)
    if(opt==1):
        name = input("Enter your name: ")
        print('''
        1. ALP
        2. ERN
        3. KZK
        ''')
        dest = int(input("Choose Option: "))
        trainId = getTrainID(dest)
        print(trainId)
        if not trainId:
            addToWaitingList()

        f = bookTicket(name, dest, trainId)
        
