# This program reads in a student percentage
# it will also round the float grade
# and prints out the corresponding grade
# it also prints the rounded grade

# author: Philip Cullen

while True:
    percentage = float(input("Please enter percentage or enter -1 to exit: "))

    if percentage == -1:
        print("Exiting Program")
        break

    if percentage < 0 or percentage > 100:
        print("Enter percentage between 0 and 100: ")
        continue

    rounded_percentage = round(percentage)
    print(f"Rounded percentage is {rounded_percentage}")

    if rounded_percentage < 40:
        print("Fail")
    elif rounded_percentage < 50:
        print("Pass")
    elif rounded_percentage < 60:
        print("Merit1")
    elif rounded_percentage < 70:
        print("Merit2")
    else:
        print("Distinction")