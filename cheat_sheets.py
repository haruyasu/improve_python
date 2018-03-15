# Cheat Sheets
# String Methods
s = "OH, my paws and whiskers!"
t = "I'm late!"

# Change Case
s.capitalize()
# 'Oh, my paws and whiskers!'

s.lower()
# 'oh, my paws and whiskers!'

s.swapcase()
# 'oh, MY PAWS AND WHISKERS!'

s.title()
# 'Oh, My Paws And Whiskers!'

s.upper()
# 'OH, MY PAWS AND WHISKERS!'

# Search
s.count('w')
# 2

s.find('w')
# 9

s.index('w')
# 9

s.rfind('w')
# 16

s.rindex('w')
# 16

s.startswith('OH')
# True

# Modify
''.join(s)
# 'OH, my paws and whiskers!'

' '.join(s)
# 'O H ,   m y   p a w s   a n d   w h i s k e r s !'

' '.join((s, t))
# "OH, my paws and whiskers! I'm late!"

s.lstrip('HO')
# ', my paws and whiskers!'

s.replace('H', 'MG')
# 'OMG, my paws and whiskers!'

s.rsplit()
# ['OH,', 'my', 'paws', 'and', 'whiskers!']

s.rsplit(' ', 1)
# ['OH, my paws and', 'whiskers!']

s.split()
# ['OH,', 'my', 'paws', 'and', 'whiskers!']

s.split(' ')
# ['OH,', 'my', 'paws', 'and', 'whiskers!']

s.splitlines()
# ['OH, my paws and whiskers!']

s.strip()
# 'OH, my paws and whiskers!'

s.strip('s!')
# 'OH, my paws and whisker'

# Format
s.center(30)
# '  OH, my paws and whiskers!   '

s.expandtabs()
# 'OH, my paws and whiskers!'

s.ljust(30)
# 'OH, my paws and whiskers!     '

s.rjust(30)
# '     OH, my paws and whiskers!'

# String Type
s.isalnum()
# False

s.isalpha()
# False

s.isprintable()
# True

s.istitle()
# False

s.isupper()
# False

s.isdecimal()
# False

s.isnumeric()
# False

text = s.replace('\n', '')
