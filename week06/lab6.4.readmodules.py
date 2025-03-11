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
