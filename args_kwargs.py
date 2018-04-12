def test(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)

args = ("a", "b", "c")
test(*args)
# arg1:  a
# arg2:  b
# arg3:  c

kwargs = {"arg1": 1, "arg2": 2, "arg3": 3}
test(**kwargs)
# arg1:  1
# arg2:  2
# arg3:  3

