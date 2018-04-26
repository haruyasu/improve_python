# Recursion
# Reverse a String
def reverse(s):
    if len(s) <= 1:
        return s

    return reverse(s[1:]) + s[0]

# print(reverse("abc"))
# cba

####
# String Permutation
def permute(s):
    out = []
    if len(s) == 1:
        out = [s]
    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i + 1:]):
                
                # print("Current letter is:", let)
                # print("perm is:", perm)
                out += [let + perm]
    return out

# print(permute("abc"))
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

####
# Fibonnaci Sequence
def fib_iter(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b
    return a

# print(fib_iter(10))
# 55

def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

# print(fib_rec(10))
# 55

n = 10
cache = [None] * (n + 1)

def fib_dyn(n):
    if n == 0 or n == 1:
        return n
    
    if cache[n] != None:
        return cache[n]
    
    cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)
    
    return cache[n]

# print(fib_dyn(10))
# 55

####
# Coin Change
def rec_coin(target, coins):
    min_coins = target
    
    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin(target - i, coins)
            if num_coins < min_coins:
                min_coins = num_coins
        
    return min_coins

# print(rec_coin(15, [1, 5, 10]))
# 2