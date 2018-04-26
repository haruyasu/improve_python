# Array Sequences

# Anagram
def anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    # print(count)
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    # print(count)
    for k in count:
        if count[k] != 0:
            return False
    return True

s1 = "dog"
s2 = "god"
# print(anagram(s1, s2))


####
# Array Pair Sum
def pair_sum(arr, k):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num, target)), max(num, target)))

    # return len(output)
    print("\n".join(map(str, list(output))))


arr = [1, 5, 2, 3]
# pair_sum(arr, 4)


####
# Find the Missing Element
def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]


arr1 = [1, 2, 3, 4]
arr2 = [1, 2, 4]
# print(finder(arr1, arr2))


####
# Largest Continuous Sum
def large_cont_sum(arr):
    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum

arr = [1, 2, -1, 3, 4, 10, 10, -10, -1]
# print(large_cont_sum(arr))


####
# Sentence Reversal
def rev_word(s):
    words = []
    length = len(s)
    spaces = [" "]

    i = 0
    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start:i])
        i += 1
    return " ".join(reversed(words))


# print(rev_word("  Hello  World Python  "))


####
# String Compression
def compress(s):
    r = ""
    length = len(s)

    if length == 0:
        return ""

    if length == 1:
        return s + "1"

    cnt = 1
    i = 1
    while i < length:
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            r = r + s[i - 1] + str(cnt)
            cnt = 1
        i += 1
    r = r + s[i - 1] + str(cnt)

    return r


# print(compress("AABBCC"))


####
# Unique Characters in String
def uni_char(s):
    return len(set(s)) == len(s)


def uni_char2(s):
    chars = set()
    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True


s = "abca"
# print(uni_char(s))


####
# Max Profit
def profit(stock_prices):
    min_stock_price = stock_prices[0]
    max_profit = 0
    for price in stock_prices:
        min_stock_price = min(min_stock_price, price)
        comparison_profit = price - min_stock_price
        max_profit = max(max_profit, comparison_profit)
    return max_profit

# print(profit([23, 12, 3, 10]))
# 7

####
# Index Prod
def index_prod(lst):
    output = [None] * len(lst)
    product = 1
    i = 0
    
    while i < len(lst):
        output[i] = product
        print(i, output, product)
        product *= lst[i]
        i += 1
    product = 1
    i = len(lst) - 1
    
    while i >= 0:
        output[i] *= product
        product *= lst[i]
        print(i, output, product)
        i -= 1
    
    return output

# print(index_prod([2, 3, 4]))
# [12, 8, 6]

####
# Overlap
def calc_overlap(coor1, dim1, coor2, dim2):
    greater = max(coor1, coor2)
    lower = min(coor1 + dim1, coor2 + dim2)
    if greater >= lower:
        return (None, None)
    overlap = lower - greater
    return (greater, overlap)

def calc_rect_overlap(r1, r2):
    x_overlap, w_overlap = calc_overlap(r1["x"], r1["w"], r2["x"], r2["w"])
    y_overlap, h_overlap = calc_overlap(r1["y"], r1["h"], r2["y"], r2["h"])
    if not w_overlap or not h_overlap:
        print("No overlap")
        return None
    return {"x": x_overlap, "y": y_overlap, "w": w_overlap, "h": h_overlap}

r1 = {"x": 2, "y": 4, "w": 5, "h": 12}
r2 = {"x": 1, "y": 5, "w": 7, "h": 14}
# print(calc_rect_overlap(r1, r2))


####
# Dice
from random import randint
def dice7():
    return randint(1, 7)
def convert7to5():
    roll = 7
    while roll > 5:
        roll = dice7()
        print("dice7() produced a roll of ", roll)
    print("Your final returned roll is below: ")
    return roll
# print(convert7to5())


####
# Dice2
def dice5():
    return randint(1, 5)
def convert5to7():
    roll_1 = dice5()
    roll_2 = dice5()
    
    num = ((roll_1 - 1) * 5) + (roll_2)
    
    # if num > 21:
    #     continue
    return num % 7 + 1

# print(convert5to7())

####
# Find Square
def sequ(num):
    if num < 0:
        raise ValueError
    if num == 1:
        return 1
    for k in range(int(num / 2) + 1):
        if k ** 2 == num:
            return k
        elif k ** 2 > num:
            return k - 1
    return k

# print(sequ(14))


####
# High Low
def sol(lst):
    high = max(lst[0], lst[1])
    low = min(lst[0], lst[1])
    high_prod2 = lst[0] * lst[1]
    low_prod2 = lst[0] * lst[1]
    high_prod3 = lst[0] * lst[1] * lst[2]
    
    for num in lst[2:]:
        high_prod3 = max(high_prod3, num * high_prod2, num * low_prod2)
        high_prod2 = max(high_prod2, num * high, num * low)
        low_prod2 = min(low_prod2, num * high, num * low)
        high = max(high, num)
        low = min(low, num)
    return high_prod3



####
# Coin change
def co(n, coins):
    arr = [1] + [0] * n
    for coin in coins:
        for i in range(coin, n + 1):
            arr[i] += arr[i - coin]
    if n == 0:
        return 0
    else:
        return arr[n]

