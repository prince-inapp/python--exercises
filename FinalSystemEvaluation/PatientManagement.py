# patient management
from codecs import getencoder
import pyodbc

conString = 'Driver={SQL Server};Server=DESKTOP-CKLRF1B\SQLEXPRESS;Database=hospital;Truseted_Connection=yes;'
conn = pyodbc.connect(conString)

def addPatient( id, name, gender, age, bloodgroup):
        cursor = conn.cursor()
        try:
            cursor.execute('insert into patients values (?,?,?,?,?)', id, name, gender, age, bloodgroup)
            conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

def updatePatient( id, name, gender, age, bloodgroup):
        cursor = conn.cursor()
        try:
            cursor.execute('update patients set patientId = ?, name = ?, gender = ?, age = ?, bloodGroup = ? where patientId = ?', (id, name, gender, age, bloodgroup, id))
            conn.commit()
            print("Details updated...")
        except:
            print("update error")

def searchPatient( id):
        cursor = conn.cursor()
        try:
            cursor.execute("select * from patients where patientId = ?", id)
            if(cursor.rowcount == 0):
                print("Patient not registered")
                return False
            else:
                for row in cursor:
                    print('''ID:{}
                            Name : {}
                            Gender :{}
                            Age: {}
                            Blood Group : {}'''.format(row[0], row[1], row[2], row[3], row[4]))
                return True
                
        except:
            print("search error")
            return False

while(True):
    print("""
        1. Add Patient
        2. Update Patient
        3. Delete Patient
        4. List Patients
        5. Search Patient
        9. Exit
        """)
    opt = int(input())
    if(opt == 1):
        try:
            id = int(input("ID: "))
            name = input("Name: ")
            gender = input("Gender: ")
            age = int(input("Age: "))
            bg = input("Blood Group: ")
            if bg in ('A+', 'B+', 'A-', 'B-', 'O+', 'O-'):
                if(addPatient(id, name, gender, age, bg)):
                    print("Patient Added")
        except Exception as e:
            print(e)
    if(opt == 2):
        id = int(input("Enter ID to Update: "))
        if(searchPatient(id)):
            try:
                id = int(input("ID: "))
                name = input("Name: ")
                gender = input("Gender: ")
                age = int(input("Age: "))
                bg = input("Blood Group: ")
                if bg in ['A+', 'B+', 'A-', 'B-', 'O+', 'O-']:
                    updatePatient(id, name, gender, age, bg)
                    
            except Exception as e:
                print(e)
    if(opt == 4):
        
        cursor = conn.cursor()
        try:
            cursor.execute("Select * from patients")
            for i in cursor:
                print("ID:{}\t\tName:{}\t\tGender: {}\t\tAge: {}\t\tBlood Group{}".format(i[0], i[1], i[2], i[3], i[4]))
        except:
            print("listing error")

    if(opt == 5):
        id = int(input("Enter ID:"))
        temp = searchPatient(id)