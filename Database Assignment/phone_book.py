import pyodbc
def displayOptions():
    print('''
    1. List all contacts
    2. Add new contact
    3. Delete contact
    4. Search contact by name
    5. Search contact by number
    6. Exit
    ''')
conString = 'Driver={SQL Server};Server=DESKTOP-CKLRF1B\SQLEXPRESS;Database=PhoneBook;Truseted_Connection=yes;'

    
def createTable():
    try:
        conn = pyodbc.connect(conString)
        myCursor = conn.cursor()
        myCursor.execute('''CREATE TABLE Contacts
        (id int identity primary key,
        Name varchar(20),
        Number varchar(20)
        );
        ''')
        conn.commit()
        return True
    except Exception as e:
        #print(type(e).__name__)
        return False


    
if(createTable()):
    print("Table Created")
else:
    print("Table Exists")        

while True:
    displayOptions()
    opt = int(input("Choose Option :"))
    match opt:
        
        case 1:
            phoneBook = dict()
            # list all contact
            try:
                conn = pyodbc.connect(conString)
                myCursor = conn.cursor()
                myCursor.execute('SELECT * FROM Contacts;')
                for row in myCursor:
                    #print(row)
                    phoneBook[row[1]] = row[2]
                #print(phoneBook)
                for key, val in phoneBook.items():
                    #print(key,val)
                    print('-------------------')
                    print('Name - ',key)
                    print('Number - ', val)
                    print('-------------------')
            except Exception as e:
                print(e)
            

        case 2:
            # add contact
            name = input("enter name :")
            number = input("enter number: ")
            try:
                conn = pyodbc.connect(conString)
                myCursor = conn.cursor()
                myCursor.execute('INSERT INTO Contacts VALUES (?, ?)',(name, number))
                conn.commit()
                print("Contact added successfully...")
            except Exception as e:
                print(type(e).__name__)
            finally:
                conn.close()
        
        case 3:
            # delete a contact
            name = input("Enter the name you want to delete: ")
            try:
                conn = pyodbc.connect(conString)
                myCursor = conn.cursor()
                myCursor.execute('DELETE FROM Contacts WHERE name = ?',(name))
                print(myCursor.fetchall())
                print("Contact Deleted")
            except Exception as e:
                print("Error... No contacts found")
                #print(e)
            finally:
                conn.close()
        
        case 4:
            # search using name
            name = input("Enter Name :")
            try:
                conn = pyodbc.connect(conString)
                myCursor = conn.cursor()
                myCursor.execute('SELECT Number from Contacts WHERE Name = ?',(name))
                number = myCursor.fetchall()
                if(len(number)!=0):
                    for i in number:
                        print(str(i[0]))
                #print(number)
                else:
                    print("No Contact Found")
            except Exception as e:
                print(e)
            finally:
                conn.close()
        
        case 5:
            # search using number
            number = input("Enter the number :")
            try:
                conn = pyodbc.connect(conString)
                myCursor = conn.cursor()
                myCursor.execute('SELECT name from Contacts WHERE Number = ?',(number))
                name = myCursor.fetchall()
                if(len(name)!=0):
                    for i in name:
                        print(i[0])
                else:
                    print("No Contact Found")
                #print(myCursor.fetchone()[0])
            except Exception as e:
                print(e)
            finally:
                conn.close()
        
        case 6:
            exit()
        
        case _:
            print("Invalid Option...")
            
            