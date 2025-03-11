def displaymenu():
    print("What would you like to do?")
    print("\t(a) Add New Student")
    print("\t(v) View Students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice 
def doadd():
    print("In adding")
def doview():
    print("In viewing")

choice = displaymenu()
while (choice != "q"):
    if choice == "a":
        doadd()
    elif choice == "v":
        doview()
    elif choice != "q":
        print("\n\nplease select either a, v, or q")
    choice = displaymenu()