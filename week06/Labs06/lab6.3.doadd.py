students = []
def readmodules():
    return[]

def doadd(students):
    currentstudent = {}
    currentstudent["name"] = input("Enter Name:")
    currentstudent["modules"] = readmodules()

doadd(students)
print(students)
