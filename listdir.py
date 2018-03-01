import os

path = 'C:/Python27/'
files = []

# search folder
for x in os.listdir(path):
    if os.path.isdir(path + x):
        files.append(x)

print(files)

############
# search files
files2 = []
for x in os.listdir(path):
    if os.path.isfile(path + x):
        files2.append(x)

print(files2)
