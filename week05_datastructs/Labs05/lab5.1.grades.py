# this program stores a students name, list of their courses and their grades
# in a dict

# author: Philip Cullen

student = {
    "name": "Philip",
    "modules" : [
        { 
            "coursename":"programming",
            "grade" : 45
        },
        {
            "coursename": "history",
            "grade" : 99
        }
    ]
}
print("Student: {}".format(student["name"]))
for module in student ["modules"]:
    print("\t {} \t: {}".format(module["coursename"], module["grade"]))


