import os


class run():
    print("\n")


    if os.path.exists("data/record/log"):
        print("log exsists.....\log creation halted.....")
    else:
        ir = open("data/record/logDev", "r")
        user = ir.read()
        ir.close()
        ua = open("data/record/log", "a")
        for a in user:
            ua.write(a)
        ua.close()
