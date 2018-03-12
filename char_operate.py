# replace()
print "Hello World!".replace("Hello", "Good")
print "Hello World!".replace(" World!", "")

# in
print "world" in "Hello"
print "world" in "Hello world"

# startswith()
print "Hello world".startswith("Hello")
print "Hello world".startswith("hello")

# endswidth()
print "Hello world".endswith("world")
print "Hello world".endswith("hello")

# find()
print "apple apple apple".find("apple")
print "apple apple apple".find("orange")

# rfing()
print "apple apple apple".rfind("apple")
print "apple apple apple".rfind("orange")

# index()
print "apple apple apple".index("apple")
#print "apple apple apple".index("orange")

# rindex()
print "apple apple apple".rindex("apple")
#print "apple apple apple".rindex("orange")

# isalnum()
print "abc123".isalnum()
print "abc 123".isalnum()

# isalpha()
print "abc123".isalpha()
print "abcdef".isalpha()

# isdigit()
print "123456".isdigit()
print "abcdef".isdigit()

# islower()
print "abc".islower()
print "ABC".islower()

# isspace()
print "  ".isspace()
print " aa bb ".isspace()

# istitle()
print "Hello World".istitle()
print "Hello world".istitle()

# capitalize()
print "hello world".capitalize()

# swapcase()
print "HeLLO world".swapcase()

# title()
print "hello world".title()

# lower()
print "HELLO WORLd".lower()

# upper()
print "hello world".upper()

# split()
print "apple orange banana grape".split()
# ['apple', 'orange', 'banana', 'grape']
print "apple,orange,banana,grape".split(",")
print "apple,orange,banana,grape".split(",", 2)

# rsplit()
print "apple orange banana grape".rsplit()
print "apple,orange,banana,grape".rsplit(",")
print "apple,orange,banana,grape".rsplit(",", 2)

# splitlines()
print "apple\norange\nbanana\ngrape".splitlines()

# sorted()
ls = ["5","2","1","4","3"]
print "".join(sorted(ls))
num = 4215
print sorted([c for c in str(num) + '0000'], reverse=True)[:4]

# set
names = ["a", "b", "a", "v", "b", "c"]
set_names = set(names)
print(set_names)
