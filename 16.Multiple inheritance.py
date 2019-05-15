class person:
    def __init__(self,personName,personAge):
        self.name=personName
        self.age=personAge

    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)

class student:
    def __init__(self,studentID):
        self.studentID=studentID

    def getID(self):
        return self.studentID

class resident(person,student):
    def __init__(self,name,age,ID):
        person.__init__(self,name,age)
        student.__init__(self,ID)

resident1= resident("John",30,"102")
resident1.showName()
print(resident1.getID())
