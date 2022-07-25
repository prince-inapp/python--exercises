import os
# phone book 
def displayOptions():
    print('''
    1. List all contacts
    2. Add new contact
    3. Delete contact
    4. Search contact by name
    5. Search contact by number
    6. Exit
    ''')

phone_book = dict()

if(os.path.isfile('contact.txt')):
    f = open('contact.txt','r')
    temp = f.readlines()
    print(temp)
    print(type(temp))
else:
    f = open('contact.txt','w')


while(True):
    displayOptions()
    option = int(input("Enter option :"))
    match option:
        case 1:
            names = []
            '''List all Contacts'''
            for name in temp:
                names.append(name.split(':')[0])
            names = sorted(names)
            for name in names:
                print(name)
        case 2:
            '''Add a new contact'''
            name = input("Enter name :")
            phone_number = input("Enter phone number :")
            phone_book[name] = phone_number
            print("Contact {} : {} added to phone book".format(name,phone_number))

        case 3:
            '''Delete a contact'''
            name = input("enter name to delete :")
            if(name in phone_book.keys()):
                del phone_book[name]
                print("contact {} deleted!...".format(name))
            else:
                print("No names found!...")
        case 4:
            '''seach by contact by name'''
            name = input("Enter name to search: ")
            if name in phone_book.keys():
                print("{}-{}".format(name,phone_book[name]))
            else:
                print("no contacts found")
        case 5:
            '''search by number'''
            number = input("Enter phone number:")
            numbers = list(phone_book.values())
            #print(numbers)
            if(number in numbers):
                pos = numbers.index(number)
                names = list(phone_book.keys())
                print("Name :",names[pos])
            else:
                print("number not found!")
        case 6:
            print("Program Exited!")
            break
