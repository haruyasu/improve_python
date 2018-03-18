from collections import Counter

data = ['aaa', 'bbb', 'ccc', 'aaa', 'ddd']
counter = Counter(data)
print(counter)
# Counter({'aaa': 2, 'bbb': 1, 'ccc': 1, 'ddd': 1})

for i in counter.values():
    print(i)
# 2
# 1
# 1
# 1

#######
mylist = ["apple", "banana", "apple", "apple", "orange"]
mycounter = Counter(mylist)
print(mycounter)
# Counter({'apple': 3, 'orange': 1, 'banana': 1})

#######
mydict = {"apple": 1, "banana": 4, "orange": 3}
mycounter = Counter(mydict)
print(mycounter)
# Counter({'banana': 4, 'orange': 3, 'apple': 1})

#######
myword = "helloworld!"
mycounter = Counter(myword)
print(mycounter)
# Counter({'l': 3, 'o': 2, '!': 1, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})

#######
phrase = "my motto is one for all all for one"
words = phrase.split()
mycounter = Counter(words)
print(mycounter)
# Counter({'all': 2, 'for': 2, 'one': 2, 'is': 1, 'motto': 1, 'my': 1})

for i in mycounter.keys():
    if i == "for":
        print(mycounter[i])
# 2

########
# collections.defaultdict
from collections import defaultdict

results3 = defaultdict(list)
for word in words:
    results3[word[0]].append(word)
print results3
# defaultdict(<type 'list'>, {'a': ['apple', 'alpha'], 'b': ['banana', 'beta'], 'o': ['orange']})
