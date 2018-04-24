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
print(uni_char(s))

