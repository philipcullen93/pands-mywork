import json
students = []
FILENAME = "testdict.json"

def writedict(obj):
    with open(FILENAME, "wt") as f:
        json.dump(obj, f)

def readdict():
    with open(FILENAME) as f:
        return json.load(f)

def displaymenu():
    print("What would you like to do?")
    print("\t(a) Add New Student")
    print("\t(v) View Students")
    print("\t(l) Load Students")
    print("\t(s) Save Students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/l/s/q):").strip()
    return choice 

def doadd():
    currentstudent = {}
    currentstudent["name"] = input("Enter Name:")
    currentstudent["modules"] = readmodules()
    students.append(currentstudent)

def doview():
    for currentstudent in students:
        print(currentstudent["name"])
        displaymodules(currentstudent["modules"])

def dosave():
    writedict(students)
    print("students saved")

def doload():
    global students 
    students = readdict()
    print ("students loaded")

def readmodules():
    modules = []
    modulename = input("\t Enter the first module name (blank to quit): ").strip()

    while modulename != "":
        module = {}
        module["name"] = modulename
        module["grade"] = int(input("\t\t Enter module grade: "))
        modules.append(module)
        modulename = input("\t Enter the next module name (blank to quit): ").strip()
    return modules

def displaymodules(modules):
    print("\tName   \tGrade")
    for module in modules:
        print(f"\t{module["name"]}  \t{module['grade']}")

choice = displaymenu()
while (choice != "q"):
    if choice == "a":
        doadd()
    elif choice == "v":
        doview()
    elif choice == "l":
        doload()
    elif choice == "s":
        dosave()
    elif choice != "q":
        print("\n\nplease select either a, v, or q")
    choice = displaymenu()