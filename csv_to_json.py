import csv
import json

json_list = []
json_data = {}

with open("F:/improve_pyhton/test.csv") as f:
    for line in csv.DictReader(f):
        json_list.append(line)

    json_data["test"] = json_list

with open("F:/improve_pyhton/test3.json", "w") as f:
    json.dump(json_data, f, indent=4)
