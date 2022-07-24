from Student import Student

def take_int_input(msg):
    try:
        num = int(input(msg))
        return num
    except ValueError or TypeError:
        print("Invalid input")
        return take_int_input(msg)

def take_marks_input(msg):
    try:
        num = float(input(msg))
        if(num>100 or num<0):
            print("Convert the marks out of 100 and try again.")
            raise Exception
        return num
    except ValueError or TypeError:
        print("Invalid input")
        return take_marks_input(msg)
    except Exception:
        return take_marks_input(msg)

class SRCMS():

    storage = {}

    def enterStudentDetails(self):
        print("Enter the student details")
        roll = take_int_input("Enter the roll number: ")
        name = input("Enter the name: ")
        maths = take_marks_input("Enter the marks in maths: ")
        physics = take_marks_input("Enter the marks in physics: ")
        chemistry = take_marks_input("Enter the marks in chemistry: ")
        english = take_marks_input("Enter the marks in english: ")
        programming = take_marks_input("Enter the marks in programming: ")
        student = Student(roll, name, maths, physics, chemistry, english, programming)
        return student

    @classmethod
    def addStudent(self, cls):
        self.storage[cls.rollNumber] = cls
        return
    
    def search_by_rollNumber(self, rollNumber):
        if rollNumber in self.storage:
            return self.storage[rollNumber]
        else:
            print("Student not found")
            return None
    
    def delete_student_rollNumber(self, rollNumber):
        if(self.search_by_rollNumber(rollNumber)!= None):
            self.storage.pop(rollNumber)
        else:
            print("Roll Number did not found.")

    def modifyMarks(self, roll):
        if(self.search_by_rollNumber(roll)!=None):
            print("Choose the subject you want to change marks.")
            print('''
            1. Maths
            2. Physics
            3. Chemistry
            4. English
            5. Programming
            ''')
            choice = take_int_input("Enter your choice: ")
            if(choice == 1):
                marks = take_marks_input("Enter the new marks for maths: ")
                self.storage[roll].mathsMark = marks
                print("Marks updated successfully")
            elif(choice == 2):
                marks = take_marks_input("Enter the new marks for physics: ")
                self.storage[roll].physicsMark = marks
                print("Marks updated successfully")
            elif(choice == 3):
                marks = take_marks_input("Enter the new marks for chemistry: ")
                self.storage[roll].chemistryMark = marks
                print("Marks updated successfully")
            elif(choice == 4):
                marks = take_marks_input("Enter the new marks for english: ")
                self.storage[roll].englishMark = marks
                print("Marks updated successfully")
            elif(choice == 5):
                marks = take_marks_input("Enter the new marks for programming: ")
                self.storage[roll].programmingMark = marks
                print("Marks updated successfully")
            else:
                print("Invalid choice")
    def displayStudentDetails(self, cls):
        print(
            '''
            Roll Number : {}
            Name : {}
            Maths Mark : {}
            Physics Mark : {}
            Chemistry Mark : {}
            English Mark : {}
            Programming Mark : {}
            '''.format(cls.rollNumber, cls.name, cls.mathsMark, cls.physicsMark, cls.chemistryMark, cls.englishMark, cls.programmingMark)
        )
    def getStatus(pself,percentage):
        if(percentage>45):
            return "Pass"
        else:
            return "Fail"
    
    def generateReportCard(self, cls):
        totalMarks = cls.mathsMark + cls.physicsMark + cls.chemistryMark + cls.englishMark + cls.programmingMark
        percentage = totalMarks / 500 * 100
        status = self.getStatus(percentage)
        print(
            '''
            Roll Number : {}
            Name : {}
            Maths Mark : {}
            Physics Mark : {}
            Chemistry Mark : {}
            English Mark : {}
            Programming Mark : {}
            Total Marks : {}
            Percentage : {}%
            Status : {}
            '''.format(cls.rollNumber, cls.name, cls.mathsMark, cls.physicsMark, cls.chemistryMark, cls.englishMark, cls.programmingMark, totalMarks, percentage, status)
        )
        print("Report Card Generated")



def menu():
    print('''
    1. create a student record
    2. delete a student record based on the roll number
    3. modify the marks in a student record given in roll number
    4. display all student records
    5. display a students record based on the roll number
    6. Generate Report Card
    7. Exit
    ''')

def main():
    srcms = SRCMS()
    while True:
        menu()
        choice = take_int_input("Enter your choice: ")
        if(choice == 1):
            student = srcms.enterStudentDetails()
            srcms.addStudent(student)
        elif(choice == 2):
            rollNumber = take_int_input("Enter the roll number: ")
            srcms.delete_student_rollNumber(rollNumber)
        elif(choice == 3):
            rollNumber = take_int_input("Enter the roll number: ")
            srcms.modifyMarks(rollNumber)
        elif(choice == 4):
            for key, value in srcms.storage.items():
                srcms.displayStudentDetails(value)
        elif(choice == 5):
            rollNumber = take_int_input("Enter the roll number: ")
            student = srcms.search_by_rollNumber(rollNumber)
            if(student != None):
                srcms.displayStudentDetails(student)
        elif(choice == 6):
            roll = take_int_input("Enter roll number :")
            student = srcms.search_by_rollNumber(roll)
            if(student != None):
                srcms.generateReportCard(student)
            else:
                print("Report Card can't be generated.")
        elif(choice == 7):
            break
        else:
            print("Invalid choice")

main()