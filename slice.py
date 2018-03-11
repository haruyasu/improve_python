# coding: utf-8
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# n番目からm-1番目の要素を取り出す
# a[n:m]

# 1番目から3番目の要素を取り出す
print a[1:4]
# [2, 3, 4]

# 始点を省略すると0番目から
print a[:3]
# [1, 2, 3]

# 終点を省略すると最後まで
print a[7:]
# [8, 9]

# -1で一番最後
print a[-1]
# 9

print a[-2:]
# [8, 9] （拡張子の取り出しなどよく使う）

# コロンを2個続けるとステップして抜き出します
print a[::3]
# [1, 4, 7]

# もちろん切り出しつつのステップも可能
print a[2:7:3]
# [3, 6]

# 負の数を使って後ろから
print a[::-3]
# [9, 6, 3]

# reverse
print a[::-1]
