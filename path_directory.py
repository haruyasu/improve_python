import os

# current directory
print os.getcwd()

# move directory
os.chdir("../")
print os.getcwd()

# file list
search = "F:/maya_python/04_pyside2/"
print os.listdir(search)

for i in os.listdir(search):
    pass
    #print i

def searchFile(root, result=[]):
    for path in os.listdir(root):
        fullpath = os.path.join(root, path)

        if os.path.isdir(fullpath):
            result = searchFile(fullpath, result)
        else:
            result.append(fullpath)
    return result

allFile = searchFile(search)

for i in allFile:
    if i.endswith(".py"):
        print os.path.basename(i)

#########
# dir or file
print os.path.isdir(search)

print os.path.isfile(search)

#########
# join
testPath = os.path.join(search, "bin", "maya.exe")
print testPath

#########
# exists
print os.path.exists(search)

#########
# get dir name
print os.path.basename(testPath)

#########
# abspath
print os.path.abspath("./")
