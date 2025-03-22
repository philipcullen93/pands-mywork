# function reads Dict from a file
#Author: Philip Cullen

import json
FILENAME = "testdict.json"

def readdict():
    # this will throw an error if the file doesn't exist
    # it should readily return an empty dict
    with open(FILENAME) as f:
        return json.load(f)

# test
somedict = readdict()
print(somedict)
