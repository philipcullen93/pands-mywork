FILENAME = "data.txt"
'''
with open(FILENAME,'rt') as f:
    for data in f:
        # print(data, end = "")
        print(data.strip())
        # print(data[:-1])
'''
with open("data2.txt","w+") as f:
    f.write("What the Hell?\n")
    f.write("Cow Now How\n")
    f.seek(0)
    data = f.read()
    print(data)

print("done")
