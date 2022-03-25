import os
import json
# Extracts the data from the json file
# Can also use sqlalchemy or pymongo instead
def extractData(path):
    if os.path.exists(path):
        try:
            with open(path) as menuFile:
                data = json.load(menuFile)
                return data
        except:
            return "failed"
    else:
        return "no such file"