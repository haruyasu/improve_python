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
# collections.defaultdict
from collections import defaultdict

results3 = defaultdict(list)
for word in words:
    results3[word[0]].append(word)
print results3
# defaultdict(<type 'list'>, {'a': ['apple', 'alpha'], 'b': ['banana', 'beta'], 'o': ['orange']})

########
# itertools.groupby
from itertools import groupby
from operator import itemgetter

results4 = {k: list(v) for k, v in groupby(sorted(words), key=itemgetter(0))}
print results4
# {'a': ['alpha', 'apple'], 'b': ['banana', 'beta'], 'o': ['orange']}

#######
from collections import Counter

mylist = ["apple","banana","apple","apple","orange"]
mycounter = Counter(mylist)
print(mycounter)
# Counter({'apple': 3, 'orange': 1, 'banana': 1})

#######
from collections import Counter

mydict = {"apple" : 1, "banana" : 4, "orange" : 3}
mycounter = Counter(mydict)
print(mycounter)
# Counter({'banana': 4, 'orange': 3, 'apple': 1})

#######
from collections import Counter

myword = "helloworld!"
mycounter = Counter(myword)
print(mycounter)
# Counter({'l': 3, 'o': 2, '!': 1, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})

#######
from collections import Counter

phrase = "my motto is one for all all for one"
words = phrase.split()
mycounter = Counter(words)
print(mycounter)
# Counter({'all': 2, 'for': 2, 'one': 2, 'is': 1, 'motto': 1, 'my': 1})

for i in mycounter.keys():
    if i == "for":
        print(mycounter[i])
# 2

#######
list = [{'Key': 'Name',     'Value': 'apple'},
        {'Key': 'Color',    'Value': 'red'},
        {'Key': 'Quantity', 'Value': 10}]

name_values = [x['Value'] for x in list if x['Key'] == 'Name']
name_value = name_values[0] if len(name_values) else ''
print(name_value)
# apple
