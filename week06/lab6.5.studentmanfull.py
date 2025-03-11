def displaymenu():
    print("What would you like to do?")
    print("\t(a) Add New Student")
    print("\t(v) View Students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

def doadd(students):
    currentstudent = {}
    currentstudent["name"] = input("Enter Name:")
    currentstudent["modules"] = readmodules()
    students.append(currentstudent)

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

def doview(students):
    for currentstudent in students:
        print(currentstudent["name"])
        displaymodules(currentstudent["modules"])

students = []
choice = displaymenu()
while (choice != "q"):
    if choice == "a":
        doadd(students)
    elif choice == "v":
        doview(students)
    elif choice != "q":
        print("\n\nplease select either a, v, or q")
    choice = displaymenu()
