import Student

class SRCMS(Student):
    def __init__(self, rollNumber, name, mathsMark, physicsMark,
                 chemistryMark, englishMark, programmingMark):
        Student.__init__(self, rollNumber, name, mathsMark, physicsMark,
                         chemistryMark, englishMark, programmingMark)
        self._totalMark = Student.mathsMark + Student.physicsMark + Student.chemistryMark + englishMark + programmingMark
        self._percentage = (self._totalMark / 500) * 100
        self._status = self.getStatus(self._percentage)

    @property
    def totalMark(self):
        return self._totalMark
    
    @property
    def percentage(self):
        return self._percentage
    
    @property
    def status(self):
        return self._status

    def getStatus(self, percentage):
        if percentage >= 45:
            return "Pass"
        else:
            return "Fail"
    
    def generateReport(self, rollNumber, name, mathsMark, physicsMark,
                       chemistryMark, englishMark, programmingMark):
        print('''
        Roll Number: {}
        Name: {}
        Maths: {}
        Physics: {}
        Chemistry: {}
        English: {}
        Programming: {}
        Total: {} / 500
        Percentage: {} %
        Status: {}
        '''.format(rollNumber, name, mathsMark, physicsMark,chemistryMark, englishMark, programmingMark,self.totalMark, self.percentage,self.status))

