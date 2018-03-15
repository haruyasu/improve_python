import re

pattern = r"ca"
text = "caabscasca"

# compile
repatter = re.compile(pattern)
matchOB = repatter.match(text)

# no compile
# match First
matchOB = re.match(pattern, text)
if matchOB:
    print matchOB.group()
# ca

# Search Anyware
matchOB = re.search(pattern, text)
if matchOB:
    print matchOB.group()
    print matchOB.start()
    print matchOB.end()
    print matchOB.span()
# ca
# 0
# 2
# (0, 2)

# findall
matchedList = re.findall(pattern, text)
if matchedList:
    print matchedList
# ['ca', 'ca', 'ca']

# pattern = r"ca"
# text = "caabscasca"
# finditer
iterator = re.finditer(pattern, text)
for match in iterator:
    print match.group()
    print match.start()
    print match.end()
    print match.span()
# ca
# 0
# 2
# (0, 2)

# ca
# 5
# 7
# (5, 7)

# ca
# 8
# 10
# (8, 10)
