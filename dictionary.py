words = ["apple", "orange", "banana", "alpha", "beta"]

results = {}
for word in words:
    key = word[0]
    if key not in results:
        results[key] = []
    results[key].append(word)
print results

########
# dict.setdefault()
results2 = {}
for word in words:
    results2.setdefault(word[0], []).append(word)
print results2

########
# collections.defaultdict
from collections import defaultdict

results3 = defaultdict(list)
for word in words:
    results3[word[0]].append(word)
print results3

########
# itertools.groupby
from itertools import groupby
from operator import itemgetter

results4 = {k: list(v) for k, v in groupby(sorted(words), key=itemgetter(0))}
print results4

########
d = {"title": "1", "user": "2", "body": "3"}
print d

dd = dict(title="1", user="2", body="3")
print dd

#######
d = dict(apple="120", banana="200", orange="300")
print d
d["apple"] = 100
print d
d.update(apple=150, banana=250, orange=350)
print d
d.update(test=100)
print d
d["python"] = "great"
print d
