original_list = list(range(10))
print original_list
# map doing one -> doing list
mapped_list = map(lambda x: x**2, original_list)
print mapped_list

########
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

print (list(map(fizz_buzz, range(1, 21))))

########
# map
items = [1, 2, 3, 4, 5]
def plus(num):
    return num + 10
print map(plus, items)

########
# lambda
print map(lambda num: num+20, items)

########
# normal
print [x + 30 for x in items]

########
# filter
print filter(lambda num: num % 2 == 1, items)

#######
# normal
print [x for x in items if x % 2 == 1]
