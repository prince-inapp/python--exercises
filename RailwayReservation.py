import dbm
import functools
import pyodbc
from abc import ABC, abstractmethod

server_one = 'DESKTOP-CKLRF1B\SQLEXPRESS'
server_two = 'LAPTOP-85QRUTE7\SQLEXPRESS'
server_ = server_two
connString = 'Driver={SQL Server};Server={'+server_+'};Database=RailwayReservation;Truseted_Connection=yes;'
#print(connString)

# conn = pyodbc.connect(connString)
# print('Connected to Database')

train = {
    101 : 'TVM-ALP',
    102 : 'TVM-ERN',
    103 : 'TVM-KZK'
}



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
            print(row)
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
def addToWaitingList(cur, name):
    cur.execute('select * from Trains')
    for row in cur.fetchall():
        waiting_list = row[4]
        if(waiting_list<2):
            print("adding to waiting list")
            cur.execute('update Trains set waiting_list = waiting_list+1 where train_id = ?', row[0])
            cur.execute('insert into WaitingList (p_name,train_name, train_id) values (?,?,?)', name,train[row[0]],row[0])
            return True
        else:
            return False
            
@dbms
def bookTicket(cur,name, dest, trainId):
    cur.execute('INSERT INTO Passengers values (?,?,?) ',(name, dest, trainId))
    cur.execute('select booked_seats from Trains where train_id = ?',(trainId))
    print("Booking Success!")
    seats = [i for i in cur.fetchall()]
    print(seats)
    seat = 0
    seat = seats[0][0] + 1
    print(seat)
    cur.execute('update Trains set booked_seats = ? where train_id = ?',(seat, trainId))
    print("success")

@dbms
def getPassengers(cur):
    cur.execute('select * from Passengers')
    for row in cur.fetchall():
        print(row)
    return cur.fetchall()

@dbms
def getWaitingList(cur):
    cur.execute('select * from WaitingList')
    for row in cur.fetchall():
        print(row)
    return cur.fetchall()

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
            if(addToWaitingList(name)):
                print("Added to Waiting List")
            else:
                print("No seats available")
        else:
            bookTicket(name, dest, trainId)
    elif(opt==2):
        result = getPassengers()
        #print(result)
    elif(opt==3):
        result = getWaitingList()
        #print(result)
    else:
        break

        
        
