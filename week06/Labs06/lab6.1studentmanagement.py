def displaymenu():
    print("What would you like to do?")
    print("\t(a) Add New Student")
    print("\t(v) View Students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice

choice = displaymenu()
print(f"You chose: {choice}")