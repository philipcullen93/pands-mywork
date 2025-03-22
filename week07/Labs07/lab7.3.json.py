# this function stores a Dict file as JSON (JavaScript Object Notation)

# Author: Philip Cullen

import json
FILENAME = "testdict.json"
sample = dict(name = "Jason", age = 23, grades = [50, 76, 98])

def writedict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj, f)

# test
writedict(sample)