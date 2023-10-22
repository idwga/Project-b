import os


class run():
    print("\n")


if os.path.exists("log/log"):
    print("log exsists.....\log creation halted.....")
else:
    ir = open("data/logDev", "r")
    user = ir.read()
    ir.close()
    ua = open("data/log", "a")
    for a in user:
        ua.write(a)
    ua.close()
