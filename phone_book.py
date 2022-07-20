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

while(True):
    displayOptions()
    option = int(input("Enter option :"))
    match option:
        case 1:
            '''List all Contacts'''
            names = sorted(phone_book.keys())
            for key in names:
                print(key)
        case 2:
            '''Add a new contact'''
            name = input("Enter name :").title()
            phone_number = input("Enter phone number :")
            phone_book[name] = phone_number
            print("Contact {} : {} added to phone book".format(name,phone_number))
        case 3:
            '''Delete a contact'''
            name = input("enter name to delete :").title()
            if(phone_book[name]==name):
                del phone_book[name]
                print("contact {} deleted!...".format(name))
            else:
                print("No names found!...")
        case 4:
            '''seach by contact by name'''
            name = input("Enter name to search: ")
            if(phone_book[name] == name):
                print("{}-{}".format(name,phone_book[name]))
            else:
                print("no contacts found")
        case 5:
            '''search by number'''
            number = input("Enter phone number:")
            numbers = phone_book.values()
            if(number in numbers):
                pos = numbers.index(number)
                names = phone_book.keys()
                print(names[pos])
            else:
                print("number not found!")
        case 6:
            print("Program Exited!")
            break