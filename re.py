import re

pattern = r"ca"
text = "caabscasca"

# compile
repatter = re.compile(pattern)
matchOB = repatter.match(text)

# no compile
# match
matchOB = re.match(pattern, text)
if matchOB:
    print matchOB.group()

# Search
matchOB = re.search(pattern, text)
if matchOB:
    print matchOB
    print matchOB.group()
    print matchOB.start()
    print matchOB.end()
    print matchOB.span()

# findall
matchedList = re.findall(pattern, text)
if matchedList:
    print matchedList

# finditer
iterator = re.finditer(pattern, text)
for match in iterator:
    print match.group()
    print match.start()
    print match.end()
    print match.span()
    
