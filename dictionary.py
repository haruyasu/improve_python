d = {'Yamada': 30, 'Suzuki': 40, 'Tanaka': 80}

for k, v in d.items():
    print k, v
# Tanaka 80
# Yamada 30
# Suzuki 40

for k in d.keys():
    print k, d[k]
# Suzuki 40
# Yamada 30
# Tanaka 80

for v in d.values():
    print v
# 80
# 30
# 40

for k, v in d.iteritems():
    print k, v
# Tanaka 80
# Yamada 30
# Suzuki 40

########
d = {"title": "1", "user": "2", "body": "3"}
print d
# {'body': '3', 'user': '2', 'title': '1'}

dd = dict(title="1", user="2", body="3")
print dd
# {'body': '3', 'user': '2', 'title': '1'}

#######
d = dict(apple="120", banana="200", orange="300")
print d
# {'orange': '300', 'banana': '200', 'apple': '120'}

d["apple"] = 100
print d
# {'orange': '300', 'banana': '200', 'apple': 100}

d.update(apple=150, banana=250, orange=350)
print d
# {'apple': 150, 'orange': 350, 'banana': 250}

d.update(test=100)
print d
# {'test': 100, 'apple': 150, 'orange': 350, 'banana': 250}

d["python"] = "great"
print d
# {'test': 100, 'apple': 150, 'orange': 350, 'banana': 250, 'python': 'great'}

######
d = {'a': 1, 'b': 2, 'c': 3}
print(max(d.values()))
# 3
print(max([(v, k) for k, v in d.items()])[1])
# c
print(max((v, k) for (k, v) in d.items())[1])
# c
print(d.items())
# [('a', 1), ('c', 3), ('b', 2)]

######
# list to dict
li1 = [("a", 3), ("b", 2), ("c", 5)]
di1 = dict(li1)
print(di1)
# {'a': 3, 'c': 5, 'b': 2}

######
# list to dict
li2 = ["a", 3, "b", 2, "c", 5]
di2 = dict(zip(li2[0::2], li2[1::2]))
print(di2)
# {'a': 3, 'c': 5, 'b': 2}

######
keys = ['a', 'b', 'c']
values = [10, 20, 30]

dic = dict(zip(keys, values))
print(dic)
# {'a': 10, 'c': 30, 'b': 20}

#######
words = ["apple", "orange", "banana", "alpha", "beta"]

results = {}
for word in words:
    key = word[0]
    if key not in results:
        results[key] = []
    results[key].append(word)
print results
# {'a': ['apple', 'alpha'], 'b': ['banana', 'beta'], 'o': ['orange']}

########
# dict.setdefault()
results2 = {}
for word in words:
    results2.setdefault(word[0], []).append(word)
print results2
# {'a': ['apple', 'alpha'], 'b': ['banana', 'beta'], 'o': ['orange']}

########
# itertools.groupby
from itertools import groupby
from operator import itemgetter

results4 = {k: list(v) for k, v in groupby(sorted(words), key=itemgetter(0))}
print results4
# {'a': ['alpha', 'apple'], 'b': ['banana', 'beta'], 'o': ['orange']}

#######
list = [{'Key': 'Name',     'Value': 'apple'},
        {'Key': 'Color',    'Value': 'red'},
        {'Key': 'Quantity', 'Value': 10}]

name_values = [x['Value'] for x in list if x['Key'] == 'Name']
name_value = name_values[0] if len(name_values) else ''
print(name_value)
# apple
