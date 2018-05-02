def test(s):
    result = False
    if len(s) % 2 != 0:
        for i in range(int((len(s) - 1) / 2)):
            if s[i] == s[len(s) - 1 - i]:
                result = True
            else:
                return False
    else:
        for i in range(int(len(s) / 2)):
            if s[i] == s[len(s) - 1 - i]:
                result = True
            else:
                return False
    return result

s = "abca"
print(test(s))
s = "acbbca"
print(test(s))
s = "abcad"
print(test(s))
s = "aba"
print(test(s))
