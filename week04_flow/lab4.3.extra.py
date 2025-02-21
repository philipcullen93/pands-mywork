# This program reads in a student percentage
# it will also round the float grade
# and prints out the corresponding grade
# it also prints the rounded grade

# author: Philip Cullen

percentage = float(input("Enter the percentage: "))

if percentage == -1:
    print("Exiting program")

rounded_percentage = round(percentage)
print(rounded_percentage)

if rounded_percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif rounded_percentage < 40:
    print("Fail")
elif rounded_percentage < 50:
    print("Pass")
elif rounded_percentage < 60:
    print("Merit1")
elif rounded_percentage < 70:
    print("Merit2")
else:
    print("Distinction")