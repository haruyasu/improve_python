import json

f = open("F:/improve_pyhton/test.json", "r")
json_dict = json.load(f)
print("json_dict:{}".format(type(json_dict)))

json_str = json.dumps(json_dict)
print("json_str:{}".format(type(json_str)))

json_dict2 = json.loads(json_str)
print("json_dict2]{}".format(type(json_dict2)))

# write
f2 = open("F:/improve_pyhton/test2.json", "w")
json.dump(json_dict2, f2)

###########
print("book1 information : {}".format(json_dict["book1"]))
print("book2 information : {}".format(json_dict["book2"]))

for x in json_dict:
    book_page = json_dict[x]["page"]
    if(book_page > 500):
        print("{0}:{1}".format(x, json_dict[x]))

###########

cost = dict(tv="100", camera="200", radio="300")
print cost
enc = json.dumps(cost)
print enc
dec = json.loads(enc)
print dec
print(dec["tv"])

###########
f = open("F:/improve_pyhton/test4.json", "r")

jsonData = json.load(f)
# print json.dumps(jsonData, sort_keys=True, indent=4)
keyList = jsonData.keys()
keyList.sort()
# print keyList

for k in keyList:
    print "[", k, "]"
    groupDict = jsonData[k]
    # print groupDict

    nameList = groupDict.keys()
    nameList.sort()
    # print nameList

    for name in nameList:
        if groupDict[name] > 50:
            print "%s's value is %d" % (name, groupDict[name])

f.close()
