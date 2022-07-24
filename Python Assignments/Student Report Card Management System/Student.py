class Student:
    def __init__(self, rollNumber, name, mathsMark, physicsMark,
                chemistryMark, englishMark, programmingMark):
        self._rollNumber = rollNumber
        self._name = name
        self._mathsMark = mathsMark
        self._physicsMark = physicsMark
        self._chemistryMark = chemistryMark
        self._englishMark = englishMark
        self._programmingMark = programmingMark
    
    @property
    def rollNumber(self):
        return self._rollNumber
    @rollNumber.setter
    def rollNumber(self, rollNumber):
        self._rollNumber = rollNumber
    @rollNumber.deleter
    def rollNumber(self):
        del self._rollNumber
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @name.deleter
    def name(self):
        del self._name

    @property
    def mathsMark(self):
        return self._mathsMark
    @mathsMark.setter
    def mathsMark(self, mathsMark):
        self._mathsMark = mathsMark
    @mathsMark.deleter
    def mathsMark(self):
        del self._mathsMark
    
    @property
    def physicsMark(self):
        return self._physicsMark
    @physicsMark.setter
    def physicsMark(self, physicsMark):
        self._physicsMark = physicsMark
    @physicsMark.deleter
    def physicsMark(self):
        del self._physicsMark
    
    @property
    def chemistryMark(self):
        return self._chemistryMark
    @chemistryMark.setter
    def chemistryMark(self, chemistryMark):
        self._chemistryMark = chemistryMark
    @chemistryMark.deleter
    def chemistryMark(self):
        del self._chemistryMark
    
    @property
    def englishMark(self):
        return self._englishMark
    @englishMark.setter
    def englishMark(self, englishMark):
        self._englishMark = englishMark
    @englishMark.deleter
    def englishMark(self):
        del self._englishMark
    
    @property
    def programmingMark(self):
        return self._programmingMark
    @programmingMark.setter
    def programmingMark(self, programmingMark):
        self._programmingMark = programmingMark
    @programmingMark.deleter
    def programmingMark(self):
        del self._programmingMark
    

    def displayStudentDetails(self):
        print(
            '''
            Roll Number : {}
            Name : {}
            Maths Mark : {}
            Physics Mark : {}
            Chemistry Mark : {}
            English Mark : {}
            Programming Mark : {}
            '''.format(self.rollNumber, self.name, self.mathsMark, self.physicsMark,)
        )