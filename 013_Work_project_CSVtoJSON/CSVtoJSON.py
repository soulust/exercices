#!usr/bin/python

import csv
import json

csvFilePath = "schedule_51.csv"
jsonFilePath = "schedule_51.json"

#Read the CSV
arr = []
fields = ["startDateTime", "endDateTime"]
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile, fieldnames = fields, restkey = "oncallMember", escapechar = "\\")
    for csvRow in csvReader:
        arr.append(csvRow)

#Write data to a JSON file
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(arr, indent=4))