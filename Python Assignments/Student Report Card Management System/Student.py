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
    def marks(self):
        return self._mathsMark, self._physicsMark, self._chemistryMark, self._englishMark, self._programmingMark
    @marks.setter
    def marks(self, mathsMark, physicsMark, chemistryMark, englishMark, programmingMark):
        self._mathsMark = mathsMark
        self._physicsMark = physicsMark
        self._chemistryMark = chemistryMark
        self._englishMark = englishMark
        self._programmingMark = programmingMark
    @marks.deleter
    def marks(self):
        del self._mathsMark
        del self._physicsMark
        del self._chemistryMark
        del self._englishMark
        del self._programmingMark